from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str
    
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    WEATHER_API_KEY: str
    
    class Config:
        env_file = ".env" # automatically load from your .env file

# cache settings instance so it's loaded only once
@lru_cache()
def get_settings():
    return Settings()
