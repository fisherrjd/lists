from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.task_list import TaskListCreate, TaskListUpdate, TaskListRead
from schemas.share import ShareCreate
from services import list_service, share_service
from auth.dependencies import get_current_user
from database import get_db
from models.user import User
from uuid import UUID

router = APIRouter(prefix="/lists", tags=["lists"])


@router.post("/", response_model=TaskListRead)
def create_list(
    list_in: TaskListCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_service.create_list(db, current_user.id, list_in)


@router.get("/", response_model=List[TaskListRead])
def get_lists(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return list_service.get_lists_for_user(db, current_user.id)


@router.get("/{list_id}", response_model=TaskListRead)
def get_list(
    list_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = list_service.get_list(db, list_id)
    if result.owner_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to access this list"
        )
    return result


@router.put("/{list_id}", response_model=TaskListRead)
def update_list(
    list_id: UUID,
    list_in: TaskListUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = list_service.get_list(db, list_id)
    if result.owner_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to update this list"
        )
    return list_service.update_list(db, list_id, list_in)


@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_list(
    list_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = list_service.get_list(db, list_id)
    if result.owner_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this list"
        )
    list_service.delete_list(db, list_id)
    return None


@router.post("/{list_id}/share", response_model=None)
def share_list(
    list_id: UUID,
    share_in: ShareCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return share_service.share_list_with_user(db, current_user.id, list_id, share_in)
