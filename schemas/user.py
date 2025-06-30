# --- Pydantic Schemas for User ---
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class UserRead(BaseModel):
    id: int
    email: str
    created_at: datetime


class UserCreate(BaseModel):
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


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
