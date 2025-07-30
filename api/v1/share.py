from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import share_service
from database import get_db
from models.user import User
from typing import List
from schemas.list_share import ListShare as ListShareSchema
from auth.dependencies import get_current_user

router = APIRouter(prefix="/shared", tags=["auth"])


# GET /shared/ : All lists shared with the current user (pending and accepted)
@router.get("/", response_model=List[ListShareSchema])
def shared_with_me(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """
    Return all lists shared with the current user (pending and accepted).
    """
    return share_service.list_shared_with_user(db, current_user.id)


# GET /shared/invites : Only pending invites for the current user
@router.get("/invites", response_model=List[ListShareSchema])
def pending_invites(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """
    Return only pending invites for the current user.
    """
    return share_service.list_invites(db, current_user.id)


# POST /shared/invites/{invite_id}/accept : Accept an invite
@router.post("/invites/{invite_id}/accept", response_model=ListShareSchema)
def accept_invite(
    invite_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    accepted = share_service.accept_invite(db, invite_id, current_user.id)
    return accepted


# POST /shared/invites/{invite_id}/reject : Reject an invite
@router.post("/invites/{invite_id}/reject")
def reject_invite(
    invite_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    share_service.reject_invite(db, invite_id, current_user.id)
    return {"detail": "Invite rejected."}
