from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .storage import get_db, create_list, get_lists, add_item, get_items

router = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}