# backend/models/user.py
from sqlalchemy import Column, String, Integer
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id            = Column(Integer, primary_key=True, autoincrement=True)
    username      = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role          = Column(String, default="public")  # ops, supplier, distributor, public
    entity_id     = Column(String, nullable=True)     # supplier_id or distributor_id