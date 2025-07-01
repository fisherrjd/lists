# --- SQLAlchemy User Model ---
from sqlmodel import Field, Relationship, SQLModel
import datetime
import uuid

# --- Pydantic Schemas for User ---
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserBase(SQLModel):
    name: str
    username: str
    email: str


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now(datetime.timezone.utc))
    task_lists = Relationship("TaskList", back_populates="owner")  # User's task lists
    shares = Relationship("ListShare", back_populates="user")  # Shared lists


class UserUpdate(SQLModel):
    email: Optional[str] = None
    password: Optional[str] = None


class UserRead(SQLModel):
    id: int
    email: str
    created_at: datetime


class UserCreate(SQLModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def password_complexity(cls, v):
        import re

        special_chars = r"!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?`~"
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters.")
        if not re.search(r"[A-Za-z]", v):
            raise ValueError("Password must include at least one letter.")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must include a number.")
        if not re.search(f"[{re.escape(special_chars)}]", v):
            raise ValueError(
                f"Password must include a special character: {special_chars}"
            )
        return v
