from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from services.inventory.enums import status

class TicketBase(BaseModel):
    event_id: UUID
    seat_number: int = Field(gt=0)
    price: float = Field(ge=0)

class TicketCreate(TicketBase):
    # When an admin creates a ticket, it defaults to Available.
    # No user_id or reserved_at is expected in the creation payload.
    status: status.TicketStatus = status.TicketStatus.AVAILABLE

class TicketResponse(TicketBase):
    id: UUID
    status: status.TicketStatus
    # These are Optional because an 'Available' ticket has no user or reservation time yet
    user_id: Optional[UUID] = None
    reserved_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)