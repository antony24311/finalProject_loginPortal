from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_access_token
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.db.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

security = HTTPBearer()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db = Depends(get_db)
):
    """
    sqlite3 正式版 current user：
    - 驗 JWT
    - 用 raw SQL 查 users table
    """

    try:
        payload = decode_access_token(token)
        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

    cursor = db.cursor()
    cursor.execute(
        "SELECT id, username FROM users WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    # 回傳 dict（不要回傳 password）
    return {
        "id": user["id"],
        "username": user["username"],
    }

