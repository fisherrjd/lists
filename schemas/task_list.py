# --- Pydantic Schemas for Auth ---
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskListRead(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    owner_id: int

class TaskListCreate(BaseModel):
    title: str
    description: str

class TaskListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None