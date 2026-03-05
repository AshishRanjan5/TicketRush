from pydantic import BaseModel, field_validator, Field
from uuid import UUID
from datetime import datetime, timezone
from enum import Enum

class Venue(str, Enum):
    BANGALORE = "Bangalore"
    DELHI = "Delhi"
    HYDERABAD = "Hyderabad"
    MUMBAI = "Mumbai"

class Event(BaseModel):
    id: UUID
    name: str = Field(min_length=1)
    venue: Venue
    date: datetime
    capacity: int = Field(gt=0)

    @field_validator("date")
    @classmethod
    def validate_date(cls, value):
        if value < datetime.now(timezone.utc):
            raise ValueError("Events date should be in future")
        
        return value
    


