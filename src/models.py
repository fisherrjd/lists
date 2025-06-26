from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: str
    username: str

class ListItem(BaseModel):
    id: str
    text: str
    completed: bool = False

class TodoList(BaseModel):
    id: str
    title: str
    user_id: str
    items: List[ListItem] = []

class CreateUserRequest(BaseModel):
    username: str

class CreateListRequest(BaseModel):
    user_id: str
    title: str

class AddItemRequest(BaseModel):
    list_id: str
    text: str
    completed: bool = False

class RemoveItemRequest(BaseModel):
    item_id: str