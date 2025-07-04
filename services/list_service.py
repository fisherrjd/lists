from models.task_list import TaskList
from sqlalchemy.orm import Session
from typing import List
from schemas.task_list import TaskListCreate, TaskListUpdate
from uuid import UUID


def create_list(db: Session, user_id: UUID, list_in: TaskListCreate) -> TaskList:
    new_list = TaskList(
        title=list_in.title, description=list_in.description, owner_id=user_id
    )
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list


def get_lists_for_user(db: Session, user_id: int) -> List[TaskList]:
    return db.query(TaskList).filter(TaskList.owner_id == user_id).all()


def get_list(db: Session, list_id: int) -> TaskList:
    result = db.query(TaskList).filter(TaskList.id == list_id).first()
    if not result:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="List not found")
    return result


def update_list(db: Session, list_id: int, list_in: TaskListUpdate) -> TaskList:
    task_list = db.query(TaskList).filter(TaskList.id == list_id).first()
    if not task_list:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="List not found")
    if list_in.title is not None:
        task_list.title = list_in.title
    if list_in.description is not None:
        task_list.description = list_in.description
    db.commit()
    db.refresh(task_list)
    return task_list


def delete_list(db: Session, list_id: int) -> None:
    task_list = db.query(TaskList).filter(TaskList.id == list_id).first()
    if not task_list:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="List not found")
    db.delete(task_list)
    db.commit()
