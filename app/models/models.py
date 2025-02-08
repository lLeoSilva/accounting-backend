from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, func, Boolean, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.models.base import Base  # ✅ Ensure Base is imported from base.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True)
    password_hash = Column(String, nullable=False)
    fname = Column(String(100), nullable=True)
    lname = Column(String(100), nullable=True)
    role = Column(String(20), nullable=False, default="user")
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"), onupdate=text("NOW()"))

    transactions = relationship("Transaction", back_populates="user")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)
    date = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="transactions")