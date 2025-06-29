from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings

# Create the SQLAlchemy engine
engine = create_engine(settings.database_url, pool_pre_ping=True)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
