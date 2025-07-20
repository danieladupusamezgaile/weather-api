from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import get_settings

settings = get_settings()

# SQLAlchemy database engine
engine = create_engine(settings.DATABASE_URL, echo=True) # connect to PostgreSQL DB via DB_URL

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # to create DB sessions per request

Base = declarative_base() # Base class for models
