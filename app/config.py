from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_url: str = "sqlite:///./todos.db"
    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()
