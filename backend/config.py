# backend/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_SECRET_KEY: str = "dev-secret-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    DATABASE_URL: str = "sqlite:///./supply_chain.db"
    ALGORAND_NODE_URL: str = "https://testnet-api.algonode.cloud"
    ALGORAND_INDEXER_URL: str = "https://testnet-idx.algonode.cloud"
    ALGORAND_APP_ID: int = 0  # Will be updated after contract deployment
    ALGORAND_SIGNER_MNEMONIC: str = ""
    MODEL_PATH: str = "ml/artifacts/isolation_forest_v1.pkl"
    ANOMALY_THRESHOLD_HIGH: float = 0.85
    ANOMALY_THRESHOLD_MEDIUM: float = 0.70
    ANOMALY_THRESHOLD_LOW: float = 0.55

    class Config:
        env_file = ".env"

settings = Settings()