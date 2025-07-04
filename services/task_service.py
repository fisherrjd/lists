from models.task import Task
from sqlalchemy.orm import Session
from schemas.task import TaskCreate, TaskUpdate
from fastapi import HTTPException
from uuid import UUID


def add_task_to_list(db: Session, list_id: UUID, task_in: TaskCreate) -> Task:
    task = Task(
        title=task_in.title,
        completed=task_in.completed,
        quantity=task_in.quantity,  # Pass quantity
        task_list_id=list_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task_id: UUID, task_in: TaskUpdate) -> Task:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task_in.title is not None:
        task.title = task_in.title
    if task_in.completed is not None:
        task.completed = task_in.completed
    if task_in.quantity is not None:
        task.quantity = task_in.quantity  # Update quantity
    db.commit()
    db.refresh(task)
    return task


def mark_task_completed(db: Session, task_id: UUID) -> Task:
    return update_task(db, task_id, TaskUpdate(completed=True))


def delete_task(db: Session, task_id: UUID) -> None:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
