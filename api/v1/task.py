from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.task import TaskCreate, TaskUpdate, TaskRead
from services import task_service
from auth.dependencies import get_current_user
from database import get_db
from models.user import User
from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/list/{list_id}", response_model=TaskRead)
def create_task(
    list_id: UUID,
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # TODO: Optionally check user owns list or has permission
    return task_service.add_task_to_list(db, list_id, task_in)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: UUID,
    task_in: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.update_task(db, task_id, task_in)


@router.post("/{task_id}/complete", response_model=TaskRead)
def mark_completed(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.mark_task_completed(db, task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task_service.delete_task(db, task_id)
    return None
