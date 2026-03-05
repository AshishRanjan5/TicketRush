from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID


class Event(Base):
    __table__ = "events"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    




