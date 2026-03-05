from pydantic import BaseModel, field_validator, EmailStr
from uuid import UUID
from datetime import datetime
import re


class User(BaseModel):
    id: UUID
    email: EmailStr
    password: str
    created_at: datetime

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