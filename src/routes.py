from fastapi import APIRouter, HTTPException
from uuid import uuid4
from .models import (
    User, TodoList, ListItem,
    CreateUserRequest, CreateListRequest, AddItemRequest, RemoveItemRequest
)
import src.storage as storage

router = APIRouter()

@router.get("/")
def get_root(user_id: str):
    return ("test")

@router.post("/users", response_model=User)
def create_user(request: CreateUserRequest):
    user_id = str(uuid4())
    user = User(id=user_id, username=request.username)
    try:
        storage.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    user = storage.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/lists", response_model=TodoList)
def create_list(request: CreateListRequest):
    list_id = str(uuid4())
    todo_list = TodoList(id=list_id, title=request.title, user_id=request.user_id, items=[])
    try:
        storage.create_list(todo_list)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return todo_list

@router.get("/users/{user_id}/lists", response_model=list[TodoList])
def get_lists_for_user(user_id: str):
    return storage.get_lists_for_user(user_id)

@router.get("/lists/{list_id}", response_model=TodoList)
def get_list(list_id: str):
    todo_list = storage.get_list(list_id)
    if not todo_list:
        raise HTTPException(status_code=404, detail="List not found")
    return todo_list

@router.post("/items", response_model=ListItem)
def add_item(request: AddItemRequest):
    item_id = str(uuid4())
    item = ListItem(id=item_id, text=request.text, completed=request.completed)
    try:
        storage.add_item(request.list_id, item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return item

@router.get("/lists/{list_id}/items", response_model=list[ListItem])
def get_items(list_id: str):
    return storage.get_items(list_id)

@router.delete("/items/{item_id}")
def remove_item(item_id: str):
    try:
        storage.remove_item(item_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"detail": "Item removed"}