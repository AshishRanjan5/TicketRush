from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, Integer, Enum as SqlEnum
from uuid import UUID, uuid4
from datetime import datetime
from typing import List

from .base import Base
from inventory.domains.enums.venue import Venue


class Event(Base):
    __tablename__ = "events"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    venue: Mapped[Venue] = mapped_column(
        SqlEnum(Venue),
        nullable=False
    )

    date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # Relationship with tickets
    tickets: Mapped[List["Ticket"]] = relationship(
        back_populates="event",
        cascade="all, delete-orphan"
    )