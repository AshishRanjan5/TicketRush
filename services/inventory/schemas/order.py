from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from services.inventory.enums import status


class OrderBase(BaseModel):
    ticket_id: UUID

class OrderCreate(OrderBase):
    # The frontend ONLY sends the ticket_id. 
    # The API Gateway will extract the user_id from the secure JWT.
    pass

class OrderResponse(OrderBase):
    id: UUID
    user_id: UUID
    status: status.OrderStatus
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)