from models.user import User
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from datetime import datetime
from auth.security import (
    hash_password,
    create_access_token as jwt_create_access_token,
    verify_password,
)
from fastapi import HTTPException, status


def register_user(db: Session, user_in: UserCreate) -> User:
    # Check if user already exists
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered."
        )
    # Hash the password
    hashed_password = hash_password(user_in.password)
    # Create user instance
    user = User(
        email=user_in.email, username=user_in.username, hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, user_in: UserLogin) -> User:
    existing = db.query(User).filter(User.username == user_in.username).first()
    if not existing or not verify_password(user_in.password, existing.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
        )
    return existing


def create_access_token(user: User) -> str:
    # You can customize payload as needed
    payload = {
        "sub": str(user.id),
        "username": str(user.username),
        "email": str(user.email),
        "created": str(user.created_at.isoformat()),
    }
    return jwt_create_access_token(payload)
