# backend/schemas/alert.py
from pydantic import BaseModel

class AlertResponse(BaseModel):
    id: str
    shipment_id: str
    risk_type: str
    severity: int
    risk_score: float
    status: str