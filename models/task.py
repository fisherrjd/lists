# --- SQLAlchemy User Model ---
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from models import Base

# --- Pydantic Schemas for User ---
from pydantic import BaseModel
from datetime import datetime as dt


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task_list_id = Column(
        Integer, ForeignKey("task_lists.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String, nullable=False)  # renamed from thing for clarity
    completed = Column(Boolean, default=False)
    quantity = Column(Integer, nullable=True)  # Optional quantity field
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(datetime.timezone.utc),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
    )

    task_list = relationship("TaskList", back_populates="tasks")


class TaskBase(BaseModel):
    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    task_list_id: int
    created_at: dt
    updated_at: dt

    class Config:
        orm_mode = True
