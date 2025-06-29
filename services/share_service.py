from models.list_share import ListShare
from sqlalchemy.orm import Session
from typing import List

def share_list_with_user(db: Session, list_id: int, user_id: int, role: str) -> ListShare:
    # TODO: Implement sharing a list with a user
    pass

def accept_invite(db: Session, invite_id: int) -> ListShare:
    # TODO: Implement accepting an invite
    pass

def reject_invite(db: Session, invite_id: int) -> None:
    # TODO: Implement rejecting an invite
    pass

def list_invites(db: Session, user_id: int) -> List[ListShare]:
    # TODO: Implement listing invites for a user
    pass
