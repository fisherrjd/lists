from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from uuid import UUID


class TaskBase(BaseModel):
    title: str
    completed: Optional[bool] = False
    quantity: Optional[int] = None  # Optional quantity field


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
    quantity: Optional[int] = None  # Optional quantity field


class TaskRead(TaskBase):
    id: UUID
    task_list_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
