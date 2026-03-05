from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, DateTime, Enum as SqlEnum, Numeric, UniqueConstraint
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

from .base import Base
from inventory.domains.enums.status import TicketStatus


class Ticket(Base):
    __tablename__ = "tickets"

    __table_args__ = (
        UniqueConstraint("event_id", "seat_number", name="unique_event_seat"),
    )

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    event_id: Mapped[UUID] = mapped_column(
        ForeignKey("events.id"),
        nullable=False
    )

    seat_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2),  # safer for money than float
        nullable=False
    )

    status: Mapped[TicketStatus] = mapped_column(
        SqlEnum(TicketStatus),
        default=TicketStatus.AVAILABLE,
        nullable=False
    )

    user_id: Mapped[Optional[UUID]] = mapped_column(
        nullable=True
    )

    reserved_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    # Relationship with Event
    event: Mapped["Event"] = relationship(
        back_populates="tickets"
    )