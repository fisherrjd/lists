# --- SQLAlchemy User Model ---
from sqlmodels import Field, Relationship, SQLModel
from typing import Optional
import datetime
import uuid


class TaskList(SQLModel, table=True):
    # __tablename__ = "task_lists"  # Table name in the database
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str  # List title
    description: Optional[str]  # Now optional
    created_at: datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc)
    )
    owner_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)  # look into more

    # Relationships (these connect to other tables/models)
    owner = Relationship("User", back_populates="task_lists")
    shares = Relationship(
        "ListShare", back_populates="task_list", cascade="all, delete-orphan"
    )
    tasks = Relationship(
        "Task", back_populates="task_list", cascade="all, delete-orphan"
    )
