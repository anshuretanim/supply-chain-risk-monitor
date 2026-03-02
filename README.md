# Supply Chain Risk Monitor

AI-powered supply chain monitoring platform with a planned Algorand-backed audit trail for high-risk supply events.

## Overview

This repository contains a full-stack scaffold for:

- Ingesting shipment events
- Scoring risk/anomaly levels
- Creating and reviewing alerts
- Recording approval evidence on Algorand (planned)
- Exposing a public verification endpoint (planned)

The backend is currently an early scaffold: core module structure exists, but many business endpoints are still TODO implementations.

## Current Status

### Implemented now

- FastAPI app bootstrapped
- CORS configured for local frontend ports
- Health endpoint available at `/health`
- Database table creation triggered on app startup
- Environment-based settings via `.env`

### Scaffolded / TODO

- Auth (`/login`, `/register`)
- Shipment CRUD routes
- Event ingestion + risk evaluation
- Alert approval + Algorand transaction write
- Public alert verification endpoint
- ML training and inference scripts
- Algorand contract deployment and contract logic

## Repository Structure

```text
supply-chain-risk-monitor/
├── backend/
│   ├── app.py                 # FastAPI app entrypoint
│   ├── config.py              # Environment/config settings
│   ├── database.py            # SQLAlchemy setup and table creation
│   ├── models/                # ORM models
│   ├── schemas/               # Pydantic schemas
│   ├── routers/               # API route modules (mostly scaffolded)
│   ├── services/              # Domain/business service layer
│   ├── ml/                    # ML pipeline modules + artifacts/data folders
│   └── algorand/              # Algorand client/contract/deploy modules
├── frontend/
│   └── src/                   # Frontend source scaffold
├── scripts/
│   ├── setup.sh               # Linux/macOS setup helper
│   ├── seed_db.py             # Demo seed stub
│   └── test_backend_e2e.py    # E2E test placeholder
├── logs/
├── requirements.txt
├── .env.example
└── README.md
```

## Prerequisites

- Python 3.10+
- `pip`
- (Optional) Bash shell to use `scripts/setup.sh`

For Windows PowerShell users, use the manual setup steps below.

## Setup

### Option A — Linux/macOS helper script

```bash
bash scripts/setup.sh
source venv/bin/activate
```

### Option B — Manual setup (Windows/PowerShell friendly)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Then edit `.env` and replace secrets/credentials before running in any shared environment.

## Running the Backend

From project root:

```bash
uvicorn backend.app:app --reload
```

Open:

- API health: `http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Snapshot (Current)

The following route modules exist but are currently placeholder implementations and are not yet wired into `backend/app.py` via `include_router(...)`:

- Auth: `/login`, `/register`
- Shipments: `/`
- Events: `/`
- Alerts: `/`, `/{alert_id}/approve`
- Public: `/verify/{alert_id}`

At this moment, only `/health` is guaranteed active from the app entrypoint.

## Configuration

Environment variables are loaded from `.env` using `pydantic-settings`.

Key variables:

- `APP_SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `DATABASE_URL`
- `ALGORAND_NODE_URL`
- `ALGORAND_INDEXER_URL`
- `ALGORAND_APP_ID`
- `ALGORAND_SIGNER_MNEMONIC`
- `MODEL_PATH`
- `ANOMALY_THRESHOLD_HIGH`
- `ANOMALY_THRESHOLD_MEDIUM`
- `ANOMALY_THRESHOLD_LOW`

## Scripts

- `scripts/setup.sh` — bootstraps venv, installs dependencies, copies `.env`
- `scripts/seed_db.py` — currently stubbed demo output
- `scripts/test_backend_e2e.py` — currently empty placeholder

## ML and Algorand Modules

- `backend/ml/train_anomaly.py` and related ML modules are placeholders for the anomaly pipeline.
- `backend/algorand/deploy.py` and contract modules are placeholders for deployment and on-chain audit recording.

## Development Notes

- Keep `.env` out of version control.
- Use a dedicated testnet account for Algorand experimentation.
- Replace default secrets before any non-local deployment.

## Suggested Next Steps

1. Register routers in `backend/app.py` using `app.include_router(...)`.
2. Implement auth and shipment/event/alert route logic.
3. Add request/response schemas and validation.
4. Implement risk scoring service integration.
5. Implement Algorand transaction write + verify flow.
6. Add backend integration tests in `scripts/test_backend_e2e.py` or a dedicated `tests/` package.

## License

This project is licensed under the terms in `LICENSE`.
