from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import os
from app.routers import auth, users
from app.db.models import init_db

app = FastAPI(title="Final Project API")

init_db()

# Security: Trusted Host Middleware (restrict allowed Host header values)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "frontend", os.getenv("ALLOWED_HOSTS", "localhost")]
)

# Security: CORS - Restrict to specific origins rather than allowing everything
allowed_origins = [
    os.getenv("FRONTEND_URL", "http://localhost:5600"),
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5600",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type", "Authorization"]
)

app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
