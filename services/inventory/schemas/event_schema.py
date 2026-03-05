from pydantic import BaseModel, Field, field_validator, ConfigDict
from uuid import UUID
from datetime import datetime, timezone
from inventory.domains.enums.venue import Venue

# 1. Base Schema (Shared attributes)
class EventBase(BaseModel):
    name: str = Field(min_length=1)
    venue: Venue
    date: datetime
    capacity: int = Field(gt=0)

    @field_validator("date")
    @classmethod
    def validate_date(cls, value):
        if value < datetime.now(timezone.utc):
            raise ValueError("Event date must be in the future")
        return value

# 2. Create Schema (What the admin sends to create an event)
class EventCreate(EventBase):
    pass

# 3. Response Schema (What the API returns to the frontend)
class EventResponse(EventBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)