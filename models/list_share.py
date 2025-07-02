from models.task_list import TaskList
from models.user import User

from sqlmodel import Field, Relationship, SQLModel
from enum import Enum
from datetime import datetime, timezone
import uuid
from typing import Optional
from sqlalchemy import Column, Enum as SAEnum


class RoleEnum(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"


class ListShare(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    task_list_id: uuid.UUID = Field(foreign_key="tasklist.id")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    role: RoleEnum = Field(sa_column=Column(SAEnum(RoleEnum), nullable=False))
    invited_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    accepted_at: Optional[datetime] = None

    task_list: Optional["TaskList"] = Relationship(back_populates="shares")
    user: Optional["User"] = Relationship(back_populates="shares")
