# Supply Chain Risk Monitor

AI-powered supply chain risk monitoring system with Algorand audit trail.

## Project Structure
supply-chain-risk-monitor/
├── backend/
│ ├── models/ # SQLAlchemy ORM models
│ ├── routers/ # FastAPI route handlers
│ ├── schemas/ # Pydantic request/response schemas
│ ├── services/ # Business logic (auth, risk engine, Algorand)
│ ├── ml/ # Machine learning module (Person 1)
│ │ ├── artifacts/ # Trained models (.pkl files)
│ │ ├── data/ # Training and demo datasets
│ │ ├── feature_engineering.py
│ │ ├── train_anomaly.py
│ │ └── inference.py
│ ├── algorand/ # Smart contract and deployment (Person 2)
│ ├── app.py # FastAPI entry point
│ ├── config.py # Configuration and settings
│ └── database.py # Database setup
├── frontend/ # React/Vue frontend (Person 3)
├── scripts/ # Helper scripts
├── requirements.txt # Python dependencies
├── .env.example # Environment variable template
└── README.md # This file


## Quick Start

### 1. Setup Environment

```bash
bash scripts/setup.sh
source venv/bin/activate

---
