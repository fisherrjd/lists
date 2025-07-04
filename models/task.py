# --- SQLAlchemy User Model ---
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from datetime import datetime, timezone

import uuid
from models.task_list import TaskList


class Task(SQLModel, table=True):
    # __tablename__ = "tasks"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    task_list_id: uuid.UUID = Field(foreign_key="tasklist.id")
    title: str
    completed: bool
    quantity: Optional[int]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    task_list: Optional["TaskList"] = Relationship(back_populates="tasks")
