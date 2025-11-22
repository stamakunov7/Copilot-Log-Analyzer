from pydantic import BaseSettings

class CLISettings(BaseSettings):
    BACKEND_URL: str = "http://localhost:8000"

settings = CLISettings()
