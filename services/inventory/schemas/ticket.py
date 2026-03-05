from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from enum import Enum

class Status(str, Enum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    BOOKED = "Booked"


class Ticket(BaseModel):
    id: UUID
    event_id: UUID
    seat_number: int = Field(gt=0)
    price: float = Field(ge=0)
    status: Status
    user_id: UUID
    reserved_at: datetime