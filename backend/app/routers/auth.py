from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.auth import RegisterSchema, LoginSchema, TokenSchema
from app.services import auth_service
from app.db.models import get_db
from app.core import security

router = APIRouter()


@router.post("/register")
def register(data: RegisterSchema, db=Depends(get_db)):
    success = auth_service.register_user(data.username, data.password, db)
    if not success:
        raise HTTPException(status_code=400, detail="帳戶名稱已存在")
    return {"message": f"User {data.username} 註冊成功"}


@router.post("/login", response_model=TokenSchema)
def login(data: LoginSchema, db=Depends(get_db)):
    user = auth_service.authenticate_user(data.username, data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="帳號或密碼不存在")
    token = auth_service.create_token_for_user(user)
    return {"access_token": token}

@router.post("/refresh")
def refresh_token(payload: dict):
    token = payload.get("refresh_token")
    if not token:
        raise HTTPException(status_code=400, detail="Refresh token required")
    try:
        data = security.decode_refresh_token(token)
        new_access_token = security.create_access_token({"sub": data["sub"], "id": data["id"]})
        return {"access_token": new_access_token, "token_type": "bearer"}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
