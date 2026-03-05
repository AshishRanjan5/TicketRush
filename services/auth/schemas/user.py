from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from uuid import UUID
from datetime import datetime
import re

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain a special character")
        return value

class UserLogin(UserCreate):
    pass

class UserResponse(UserBase):
    id: UUID
    created_at: datetime

    # This bridge tells Pydantic to read data from SQLAlchemy model objects
    model_config = ConfigDict(from_attributes=True)