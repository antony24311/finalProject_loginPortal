import sqlite3
from app.core.config import settings

DATABASE_URL = settings.DATABASE


def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
