# --- SQLAlchemy User Model ---
from sqlmodels import Field, Relationship, SQLModel
from typing import Optional
import datetime
import uuid


class Task(SQLModel):
    # __tablename__ = "tasks"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    task_list_id: uuid.UUID = Field(foreign_key="tasklist.id")
    title: str
    completed: bool
    quantity: Optional[int]
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc), primary_key=True
    )
    updated_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc), primary_key=True
    )

    task_list = Relationship("TaskList", back_populates="tasks")
