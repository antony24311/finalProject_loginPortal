import sqlite3
from app.core.config import settings
from pathlib import Path
DATABASE = settings.DATABASE


BASE_DIR = Path(__file__).resolve().parent  # backend/
DB_PATH = BASE_DIR / settings.DATABASE     # backend/data.db

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
