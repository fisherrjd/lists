# --- SQLAlchemy User Model ---
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from models import Base

class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    email = Column(String, unique=True, index=True, nullable=False)  # User's email
    hashed_password = Column(String, nullable=False)  # Hashed password
    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # When the user was created

    # Relationships (these connect to other tables/models)
    task_lists = relationship("TaskList", back_populates="owner")  # User's task lists
    shares = relationship("ListShare", back_populates="user")  # Shared lists

# --- Pydantic Schemas for User ---
from pydantic import BaseModel
from datetime import datetime as dt

class UserBase(BaseModel):
    email: str  # Only the email field

class UserCreate(UserBase):
    password: str  # Used for registration (plain password, will be hashed)

class UserRead(UserBase):
    id: int
    created_at: dt

    class Config:
        orm_mode = True  # Allows Pydantic to work with SQLAlchemy models
