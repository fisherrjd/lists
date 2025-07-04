from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import share_service
from database import get_db
from models.user import User
from typing import List
from schemas.list_share import ListShare as ListShareSchema
from auth.dependencies import get_current_user

router = APIRouter(prefix="/invites", tags=["auth"])


@router.get("/", response_model=List[ListShareSchema])
def invites(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    invites = share_service.list_invites(db, current_user.id)

    return invites


@router.post("/{invite_id}/accept")
def accept():
    pass


@router.post("/{invite_id}/reject")
def reject():
    pass
