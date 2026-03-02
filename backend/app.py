# backend/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import create_tables

app = FastAPI(
    title="Supply Chain Risk Monitor API",
    description="AI-powered anomaly detection + Algorand ARC-28 audit trail",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/health")
def health():
    return {"status": "ok", "service": "supply-chain-risk-monitor"}