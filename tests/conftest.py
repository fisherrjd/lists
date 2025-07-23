# tests/conftest.py
import os
import sqlite3
import pytest
import uuid
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from alembic.config import Config
from alembic import command
from main import app
from database import get_db

DB_PATH = os.path.join(os.path.dirname(__file__), "pytest.db")
TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}?check_same_thread=False"


@pytest.fixture(scope="session")
def test_db_engine():
    # Create the file if it does not exist
    open(DB_PATH, "a").close()

    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

    # keep a dummy connection so SQLite will not delete the file
    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, sqlite3.Connection):
            # keep one persistent connection
            pass

    # migrations
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", TEST_SQLALCHEMY_DATABASE_URL)
    command.upgrade(alembic_cfg, "head")

    yield engine
    engine.dispose()


# ------------------------------------------------------------------
# 3) Fresh session for every test
# ------------------------------------------------------------------
@pytest.fixture(scope="function")
def db_session(test_db_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_db_engine)
    session = SessionLocal()
    yield session
    session.close()


# ------------------------------------------------------------------
# 4) FastAPI TestClient that always uses the test session
# ------------------------------------------------------------------
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


# ------------------------------------------------------------------
# 5) Fixture to register 3 users and provide their info
# ------------------------------------------------------------------
import uuid


@pytest.fixture(scope="function")
def registered_users(client):
    users = []
    for i in range(3):
        unique = str(uuid.uuid4())[:8]
        username = f"testuser_{i}_{unique}"
        email = f"{username}@example.com"
        password = "Testpass123!"
        payload = {"email": email, "username": username, "password": password}
        response = client.post("/auth/register", json=payload)
        assert response.status_code in (200, 201)
        data = response.json()
        # Login to get access token
        login_payload = {"username": username, "password": password}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        login_response = client.post("/auth/login", data=login_payload, headers=headers)
        assert login_response.status_code in (200, 201)
        token = login_response.json().get("access_token") or login_response.json().get(
            "token"
        )
        assert token
        users.append(
            {
                "username": username,
                "email": email,
                "password": password,
                "id": data.get("id"),
                "access_token": token,
            }
        )
    return users
