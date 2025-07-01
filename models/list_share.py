from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
import datetime
from models import Base


class RoleEnum(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"


class ListShare(Base):
    __tablename__ = "list_shares"
    id = Column(Integer, primary_key=True, index=True)
    task_list_id = Column(
        Integer, ForeignKey("task_lists.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String, nullable=False)  # Should match RoleEnum values
    invited_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    accepted_at = Column(DateTime, nullable=True)

    # Relationships
    task_list = relationship("TaskList", back_populates="shares")
    user = relationship("User", back_populates="shares")
