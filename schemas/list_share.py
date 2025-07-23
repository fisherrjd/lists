from enum import Enum
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class RoleEnum(str, Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"


class ListShare(BaseModel):
    id: UUID
    task_list_id: UUID
    user_id: UUID
    role: RoleEnum
    invited_at: datetime
    accepted_at: Optional[datetime] = None
