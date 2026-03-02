# backend/services/auth_service.py
# TODO: Implement JWT authentication

def verify_password(plain, hashed):
    return True  # Placeholder

def create_access_token(data: dict) -> str:
    return "placeholder_token"

def get_current_user(token: str):
    return {"id": 1, "username": "user", "role": "ops"}