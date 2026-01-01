from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from app.db.database import get_db

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict, expires_delta: int = ACCESS_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    # print("SECRET_KEY =", settings.SECRET_KEY)
    # print("TYPE =", type(settings.SECRET_KEY))
    # print("SECRET_KEY =", SECRET_KEY)
    # print("TYPE =", type(SECRET_KEY))
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict, expires_delta: int = REFRESH_EXPIRE_DAYS):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def decode_refresh_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

<<<<<<< HEAD

MAX_ATTEMPTS = 5
LOCK_TIME = timedelta(minutes=5)
login_attempts = {}


def check_login(username: str):
    record = login_attempts.get(username)
    if record:
        count, locked_until = record
        return locked_until and datetime.now(timezone.utc) < locked_until


def fail_login(username: str):
    count, locked_until = login_attempts.get(username, (0, None))
    count += 1
    if count >= MAX_ATTEMPTS:
        locked_until = datetime.now(timezone.utc) + LOCK_TIME
    login_attempts[username] = (count, locked_until)


def success_login(username: str):
    login_attempts.pop(username, None)
=======
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
>>>>>>> b3d3cd4 (docker 虛擬化，前端機入JWT驗證)
