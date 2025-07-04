from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from core.config import settings
import pytest


def test_database_connection():
    engine = create_engine(settings.database_url)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
