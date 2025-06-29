from enum import Enum
from typing import List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from core.config import settings  # adjust if needed from models.user import User
from models.list_share import ListShare, RoleEnum
from models.task_list import TaskList
from auth.security import verify_token  # adjust if needed
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = verify_token(token)
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user

def require_role(
    task_list_id: int,
    required_roles: List[RoleEnum],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if user is owner of the list
    task_list = db.query(TaskList).filter(TaskList.id == task_list_id).first()
    if task_list and task_list.owner_id == current_user.id:
        return RoleEnum.owner
    share = db.query(ListShare).filter(
        ListShare.task_list_id == task_list_id,
        ListShare.user_id == current_user.id,
        ListShare.accepted_at.isnot(None)  # Only accepted invites
    ).first()
    if not share or share.role not in [role.value for role in required_roles]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    return RoleEnum(share.role)
