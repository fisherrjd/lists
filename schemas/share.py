from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .list_share import RoleEnum

class ShareRead(BaseModel):
    id: int
    task_list_id: int
    user_id: int
    role: RoleEnum
    invited_at: datetime
    accepted_at: Optional[datetime] = None

class ShareCreate(BaseModel):
    task_list_id: int
    user_id: int
    role: RoleEnum

class ShareUpdate(BaseModel):
    accepted_at: Optional[datetime] = None
    role: Optional[RoleEnum] = None
