from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from app.models import models  # Ensure models are loaded first
from app.models.base import Base  # Now import Base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()