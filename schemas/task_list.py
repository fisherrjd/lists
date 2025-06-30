# --- Pydantic Schemas for Auth ---
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from schemas.task import TaskRead
from schemas.share import ShareRead


class TaskListRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    owner_id: int
    tasks: List[TaskRead] = []
    shares: List[ShareRead] = []

    model_config = {"from_attributes": True}


class TaskListCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskListUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
