from fastapi import APIRouter, Depends
from app.deps import get_current_user

router = APIRouter()

@router.get("/me")
def read_current_user(current_user: dict = Depends(get_current_user)):
    return {"id": current_user["id"], "username": current_user["username"]}
