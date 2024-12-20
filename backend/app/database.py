from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
