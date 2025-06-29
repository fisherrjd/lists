# --- Pydantic Schemas for User ---
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserRead(BaseModel):
    id: int
    email: str
    created_at: datetime

class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

