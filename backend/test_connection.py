from app.database import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            print("Result:", list(result))
    except Exception as e:
        print("❌ Failed to connect to the database.")
        print("Error:", e)

if __name__ == "__main__":
    test_connection()