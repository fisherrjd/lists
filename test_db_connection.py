from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from core.config import settings

def test_database_connection():
    engine = create_engine(settings.database_url)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connection successful!")
    except OperationalError as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    test_database_connection()
