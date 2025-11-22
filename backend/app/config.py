import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./dev.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")

settings = Settings()
