from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import pytest


def test_database_connection(test_db_engine):
    try:
        with test_db_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
