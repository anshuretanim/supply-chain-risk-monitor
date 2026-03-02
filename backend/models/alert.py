# backend/models/alert.py
from sqlalchemy import Column, String, Float, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base
import uuid

class Alert(Base):
    __tablename__ = "alerts"
    
    id                = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    shipment_id       = Column(String, ForeignKey("shipments.id"), index=True)
    
    # ML output
    risk_type         = Column(String)   # e.g., INVOICE_FRAUD, DELAY, etc.
    severity          = Column(Integer)  # 1–5
    risk_score        = Column(Float)    # 0.0–1.0
    triggered_rules   = Column(JSON)     # list of rules that fired
    anomaly_score_raw = Column(Float)
    model_version     = Column(String)
    
    # Lifecycle
    status            = Column(String, default="pending")  # pending, approved, on_chain
    
    # On-chain proof
    algorand_app_id   = Column(Integer, nullable=True)
    algorand_tx_id    = Column(String, nullable=True)
    algorand_round    = Column(Integer, nullable=True)
    offchain_hash     = Column(String, nullable=True)
    
    created_at = Column(DateTime, server_default=func.now())
    
    shipment = relationship("Shipment", back_populates="alerts")