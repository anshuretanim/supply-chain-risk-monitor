# backend/models/shipment.py
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base

class Shipment(Base):
    __tablename__ = "shipments"
    
    id                    = Column(String, primary_key=True, index=True)
    supplier_id           = Column(String, index=True)
    distributor_id        = Column(String, index=True)
    route                 = Column(String)
    product_category      = Column(String)
    carrier_id            = Column(String)
    value_usd             = Column(Float)
    quantity_ordered      = Column(Integer)
    quantity_received     = Column(Integer, nullable=True)
    weight_kg             = Column(Float)
    
    # TODO: Add all 5 new feature columns from Part 1:
    # invoice_amount, expected_amount, invoice_deviation, quantity_mismatch,
    # route_changed, temperature_breach, planned_duration_days, etc.
    
    status                = Column(String, default="created")
    created_at            = Column(DateTime, server_default=func.now())
    updated_at            = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    events = relationship("ShipmentEvent", back_populates="shipment")
    alerts = relationship("Alert", back_populates="shipment")