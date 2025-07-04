# --- Pydantic Schemas for Auth ---
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone
from schemas.task import TaskRead
from schemas.share import ShareRead
from uuid import UUID


class TaskListRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    owner_id: UUID
    tasks: List[TaskRead] = []
    shares: List[ShareRead] = []
    model_config = {"from_attributes": True}


class TaskListCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
