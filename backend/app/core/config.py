import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

    DATABASE = os.getenv("DATABASE", "data.db")

    # HOST = os.getenv("HOST", "127.0.0.1")
    # PORT = os.getenv("PORT", "8000")


settings = Config()

if not settings.SECRET_KEY:
    print("WARNING: SECRET_KEY not found. Please set it in backend/.env")
