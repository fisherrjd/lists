# --- SQLAlchemy User Model ---
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from models import Base

class TaskList(Base):
    __tablename__ = "task_lists"  # Table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Unique user ID
    title = Column(String, index=True, nullable=False)  # List title
    description = Column(String, nullable=False)  # Hashed password
    created_at = Column(DateTime, default=datetime.datetime.utcnow)  # When the user was created
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships (these connect to other tables/models)
    owner = relationship("User", back_populates="task_lists")
    shares = relationship("ListShare", back_populates="task_list")
    tasks = relationship("Task", back_populates="task_list")

# --- Pydantic Schemas for User ---
from pydantic import BaseModel
from datetime import datetime as dt

class ListBase(BaseModel):
    title: str
    description: str

class ListCreate(ListBase):
    pass  # For now, just name and description

class ListRead(ListBase):
    id: int
    created_at: dt
    updated_at: dt
    owner_id: int

    class Config:
        orm_mode = True