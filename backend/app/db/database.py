import sqlite3
from app.core.config import settings
from contextlib import contextmanager

DATABASE_URL = settings.DATABASE


# @contextmanager
# def get_db_context():
#     """Context manager for database connections"""
#     conn = sqlite3.connect(DATABASE_URL, check_same_thread=False, timeout=5.0)
#     conn.row_factory = sqlite3.Row
#     try:
#         yield conn
#     finally:
#         conn.close()


def get_db():
    """Dependency provider for FastAPI - returns a fresh connection"""
    conn = sqlite3.connect(DATABASE_URL, check_same_thread=False, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")  # Enable WAL mode for better concurrency
    try:
        yield conn
    finally:
        conn.close()
