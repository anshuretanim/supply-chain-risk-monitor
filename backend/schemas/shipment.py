# backend/schemas/shipment.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ShipmentCreate(BaseModel):
    shipment_id: str
    supplier_id: str
    # TODO: Add all fields from Part 2 specs once Person 1 finalizes schema

class ShipmentResponse(BaseModel):
    id: str
    supplier_id: str
    # TODO: Add response fields