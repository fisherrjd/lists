from models.list_share import ListShare, RoleEnum
from sqlalchemy.orm import Session
from typing import List
from schemas.share import ShareCreate, ShareUpdate
from uuid import UUID


def share_list_with_user(
    db: Session, owner_id: UUID, list_id: UUID, share_in: ShareCreate
) -> ListShare:
    # Optionally, check if the user to share with is not the owner
    if share_in.user_id == owner_id:
        raise ValueError("Cannot share a list with yourself.")
    # Check if a share already exists
    existing = (
        db.query(ListShare)
        .filter(
            ListShare.task_list_id == list_id, ListShare.user_id == share_in.user_id
        )
        .first()
    )
    if existing:
        raise ValueError("User already invited to this list.")
    # Create the share invite
    new_share = ListShare(
        task_list_id=list_id, user_id=share_in.user_id, role=share_in.role
    )
    db.add(new_share)
    db.commit()
    db.refresh(new_share)
    return new_share


def accept_invite(db: Session, invite_id: str, user_id: str) -> ListShare:
    # Find the invite
    invite = db.query(ListShare).filter(ListShare.id == invite_id).first()
    if not invite:
        raise ValueError("Invite not found.")
    if str(invite.user_id) != str(user_id):
        raise ValueError("Not authorized to accept this invite.")
    if invite.accepted_at is not None:
        raise ValueError("Invite already accepted.")
    from datetime import datetime, timezone

    invite.accepted_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(invite)
    return invite


def reject_invite(db: Session, invite_id: str, user_id: str) -> None:
    invite = db.query(ListShare).filter(ListShare.id == invite_id).first()
    if not invite:
        raise ValueError("Invite not found.")
    if str(invite.user_id) != str(user_id):
        raise ValueError("Not authorized to reject this invite.")
    if invite.accepted_at is not None:
        raise ValueError("Cannot reject an already accepted invite.")
    db.delete(invite)
    db.commit()


def list_invites(db: Session, user_id: UUID) -> List[ListShare]:
    invites = (
        db.query(ListShare)
        .filter(ListShare.user_id == user_id, ListShare.accepted_at is None)
        .all()
    )
    return invites
