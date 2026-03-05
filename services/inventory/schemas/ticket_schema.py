from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional
from decimal import Decimal

from inventory.domains.enums.status import TicketStatus


class TicketBase(BaseModel):
    event_id: UUID
    seat_number: int = Field(gt=0)
    price: Decimal = Field(ge=0)


class TicketCreate(TicketBase):
    # Admin only provides base ticket info
    pass


class TicketResponse(TicketBase):
    id: UUID
    status: TicketStatus
    user_id: Optional[UUID] = None
    reserved_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)