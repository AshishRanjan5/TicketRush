from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum

class Status(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Order(BaseModel):
    id: UUID
    user_id: UUID
    ticket_id: UUID
    status: Status
    created_at: datetime