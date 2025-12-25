from app.core.security import hash_password, verify_password, create_access_token
from app.db.models import get_db


def register_user(username: str, password: str, db):
    cursor = db.cursor()
    existing = cursor.execute("SELECT id FROM users WHERE username=?", (username,)).fetchone()
    if existing:
        return None

    hashed = hash_password(password)
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    db.commit()
    return True


def authenticate_user(username: str, password: str, db):
    cursor = db.cursor()
    user = cursor.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if not user:
        return None
    if not verify_password(password, user["password"]):
        return None
    return {"id": user["id"], "username": user["username"]}


def create_token_for_user(user):
    token = create_access_token({"sub": user["username"], "id": user["id"]})
    return token
