# --- Pydantic Schemas for Auth ---
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class RegisterRequest(SQLModel, table=True):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str  # user id or email
    exp: int  # expiration timestamp
