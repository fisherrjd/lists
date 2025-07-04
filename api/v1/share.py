from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from services import auth_service
from database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/invites", tags=["auth"])


@router.get("/")
def invites():
    pass


@router.post("/{invite_id}/accept")
def accept():
    pass


@router.post("/{invite_id}/reject")
def reject():
    pass
