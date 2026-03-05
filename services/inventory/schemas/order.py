from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"

class OrderBase(BaseModel):
    ticket_id: UUID

class OrderCreate(OrderBase):
    # The frontend ONLY sends the ticket_id. 
    # The API Gateway will extract the user_id from the secure JWT.
    pass

class OrderResponse(OrderBase):
    id: UUID
    user_id: UUID
    status: OrderStatus
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)