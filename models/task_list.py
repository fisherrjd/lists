# --- SQLAlchemy User Model ---
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
import datetime
import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .task import Task
    from .list_share import ListShare
    from .user import User


class TaskList(SQLModel, table=True):
    # __tablename__ = "task_lists"  # Table name in the database
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str  # List title
    description: Optional[str]  # Now optional
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc)
    )
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)  # look into more

    # Relationships (these connect to other tables/models)
    owner: "User" = Relationship(back_populates="task_lists")
    shares: list["ListShare"] = Relationship(back_populates="task_list")
    tasks: list["Task"] = Relationship(back_populates="task_list")
