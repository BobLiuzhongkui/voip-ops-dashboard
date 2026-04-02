"""Application configuration."""
from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    PROJECT_NAME: str = "VoIP Operations Dashboard API"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = "development"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "voipadmin"
    POSTGRES_PASSWORD: str = "voipadmin"
    POSTGRES_DB: str = "voip_ops"
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_uri(cls, v: str | None, info) -> str:
        if isinstance(v, str): return v
        d = info.data
        return f"postgresql://{d['POSTGRES_USER']}:{d['POSTGRES_PASSWORD']}@{d['POSTGRES_SERVER']}:{d['POSTGRES_PORT']}/{d['POSTGRES_DB']}"

    SECRET_KEY: str = "change-me-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"


settings = Settings()
