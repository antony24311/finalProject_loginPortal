from fastapi import APIRouter, Depends, HTTPException, Request, status
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.schemas.auth import RegisterSchema, LoginSchema, TokenSchema
from app.services import auth_service
from app.db.models import get_db
from app.core import security

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)


@router.post("/register")
@limiter.limit("5/minute")
async def register(request: Request, data: RegisterSchema, db=Depends(get_db)):
    success = auth_service.register_user(data.username, data.password, db)
    if not success:
        # Generic error message - avoid username enumeration
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Registration failed")
    return {"message": "Registration successful"}


@router.post("/login", response_model=TokenSchema)
@limiter.limit("5/minute")
async def login(request: Request, data: LoginSchema, db=Depends(get_db)):
    if security.check_login(data.username):
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many attempts")
    user = auth_service.authenticate_user(data.username, data.password, db)
    if not user:
        security.fail_login(data.username)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    security.success_login(data.username)
    token = auth_service.create_token_for_user(user)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/refresh")
async def refresh_token(payload: dict):
    token = payload.get("refresh_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Refresh token required")
    try:
        data = security.decode_refresh_token(token)
        new_access_token = security.create_access_token({"sub": data.get("sub"), "id": data.get("id")})
        return {"access_token": new_access_token, "token_type": "bearer"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired refresh token")
