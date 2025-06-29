from models.user import User
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from auth.security import get_password_hash, create_access_token as jwt_create_access_token
from fastapi import HTTPException, status


def register_user(db: Session, user_request: UserCreate) -> User:
    # Check if user already exists
    existing = db.query(User).filter(User.email == user_request.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    # Hash the password
    hashed_password = get_password_hash(user_request.password)
    # Create user instance
    user = User(
        email=user_request.email,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, user_request: UserCreate) -> User:
    existing = db.query(User).filter(User.email == user_request.email).first()
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    if not verify_password(user_request.password, existing.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )
    return existing

def create_access_token(user: User) -> str:
    # You can customize payload as needed
    payload = {"sub": str(user.id)}
    return jwt_create_access_token(payload)
