# backend/routers/public.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/verify/{alert_id}")
def verify_alert(alert_id: str):
    # TODO: Implement public verification
    return {"verified": False, "reason": "Not yet implemented"}