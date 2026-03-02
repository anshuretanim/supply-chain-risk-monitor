# backend/routers/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    # TODO: Implement JWT login
    return {"access_token": "placeholder", "role": "ops"}

@router.post("/register")
def register(username: str, password: str):
    # TODO: Implement user registration
    return {"message": "User created"}