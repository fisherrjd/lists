from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone
from .list_share import RoleEnum
from uuid import UUID


class ShareRead(BaseModel):
    id: UUID
    task_list_id: UUID
    user_id: UUID
    role: RoleEnum
    invited_at: datetime
    accepted_at: Optional[datetime] = None


class ShareCreate(BaseModel):
    task_list_id: UUID
    user_id: UUID
    role: RoleEnum


class ShareUpdate(BaseModel):
    accepted_at: Optional[datetime] = None
    role: Optional[RoleEnum] = None
