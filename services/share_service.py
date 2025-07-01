from models.list_share import ListShare, RoleEnum
from sqlalchemy.orm import Session
from typing import List
from schemas.share import ShareCreate, ShareUpdate


def share_list_with_user(db: Session, share_in: ShareCreate) -> ListShare:
    # TODO: Implement sharing a list with a user
    pass


def accept_invite(db: Session, invite_id: int, update_in: ShareUpdate) -> ListShare:
    # TODO: Implement accepting an invite
    pass


def reject_invite(db: Session, invite_id: int) -> None:
    # TODO: Implement rejecting an invite
    pass


def list_invites(db: Session, user_id: int) -> List[ListShare]:
    # TODO: Implement listing invites for a user
    pass
