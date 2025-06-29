from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from models import Base

class ListShare(Base):
    __tablename__ = "list_shares"
    id = Column(Integer, primary_key=True, index=True)
    task_list_id = Column(Integer, ForeignKey("task_lists.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String, nullable=False)
    invited_at = Column(DateTime, default=datetime.datetime.utcnow)
    accepted_at = Column(DateTime, nullable=True)

    # Relationships
    task_list = relationship("TaskList", back_populates="shares")
    user = relationship("User", back_populates="shares")