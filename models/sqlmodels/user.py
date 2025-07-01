# --- SQLAlchemy User Model ---
from sqlmodels import Field, Relationship, SQLModel
import datetime
import uuid


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now(datetime.timezone.utc))
    task_lists = Relationship("TaskList", back_populates="owner")  # User's task lists
    shares = Relationship("ListShare", back_populates="user")  # Shared lists
