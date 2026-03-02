# backend/models/event.py
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base
import uuid

class ShipmentEvent(Base):
    __tablename__ = "shipment_events"
    
    id            = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    shipment_id   = Column(String, ForeignKey("shipments.id"), index=True)
    status        = Column(String)       # "picked_up", "in_transit", "customs", "delivered"
    location      = Column(String, nullable=True)
    notes         = Column(String, nullable=True)
    timestamp     = Column(DateTime, server_default=func.now())
    
    shipment = relationship("Shipment", back_populates="events")