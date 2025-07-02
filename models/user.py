# --- SQLAlchemy User Model ---
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime, timezone
import uuid
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .task_list import TaskList
    from .list_share import ListShare


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str
    username: str
    hashed_password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    task_lists: list["TaskList"] = Relationship(
        back_populates="owner"
    )  # User's task lists
    shares: list["ListShare"] = Relationship(back_populates="user")  # Shared lists
