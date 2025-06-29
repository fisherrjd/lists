from models.task import Task
from sqlalchemy.orm import Session
from typing import List
from schemas.task import TaskCreate, TaskUpdate

def add_task_to_list(db: Session, list_id: int, task_in: TaskCreate) -> Task:
    # TODO: Implement adding a task to a list
    pass

def update_task(db: Session, task_id: int, task_in: TaskUpdate) -> Task:
    # TODO: Implement updating a task
    pass

def mark_task_completed(db: Session, task_id: int) -> Task:
    # TODO: Implement marking a task as completed
    pass

def delete_task(db: Session, task_id: int) -> None:
    # TODO: Implement deleting a task
    pass
