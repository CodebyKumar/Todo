from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    database_url: str = "sqlite:///./todos.db"
    host: str = "0.0.0.0"
    port: int = int(os.getenv("PORT", 5000))  # Use Render's PORT env var or default to 5000
    debug: bool = False  # Set to False for production
    
    class Config:
        env_file = ".env"


settings = Settings()
