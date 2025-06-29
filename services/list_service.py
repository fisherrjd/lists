from models.task_list import TaskList
from sqlalchemy.orm import Session
from typing import List
from schemas.task_list import TaskListCreate, TaskListUpdate

def create_list(db: Session, user_id: int, list_in: TaskListCreate) -> TaskList:
    # TODO: Implement list creation
    pass

def get_lists_for_user(db: Session, user_id: int) -> List[TaskList]:
    # TODO: Implement fetching all lists for a user
    pass

def get_list(db: Session, list_id: int) -> TaskList:
    # TODO: Implement fetching a single list
    pass

def update_list(db: Session, list_id: int, list_in: TaskListUpdate) -> TaskList:
    # TODO: Implement updating a list
    pass

def delete_list(db: Session, list_id: int) -> None:
    # TODO: Implement deleting a list
    pass
