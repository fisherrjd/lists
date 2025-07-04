import os
from dotenv import load_dotenv
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from database import get_db
from alembic.config import Config
from alembic import command

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=env_path)

# Build the test database URL from .env values
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
PGPORT = os.environ.get("PGPORT", "5432")

if POSTGRES_PASSWORD:
    TEST_SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{PGPORT}/{POSTGRES_DB}"
else:
    TEST_SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}@{POSTGRES_HOST}:{PGPORT}/{POSTGRES_DB}"
    )


@pytest.fixture(scope="session")
def test_db_engine():
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
    # Run Alembic migrations
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_SQLALCHEMY_DATABASE_URL)
    command.upgrade(alembic_cfg, "head")
    yield engine
    # Optionally, clean up test DB after tests


@pytest.fixture(scope="function")
def db_session(test_db_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_db_engine)
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
