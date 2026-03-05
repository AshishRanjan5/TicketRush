from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, Enum as SqlEnum
from sqlalchemy.sql import func
from uuid import UUID, uuid4
from datetime import datetime

from .base import Base
from inventory.domains.enums.status import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

    ticket_id: Mapped[UUID] = mapped_column(
        ForeignKey("tickets.id"),
        nullable=False
    )

    user_id: Mapped[UUID] = mapped_column(
        nullable=False
    )

    status: Mapped[OrderStatus] = mapped_column(
        SqlEnum(OrderStatus),
        default=OrderStatus.PENDING,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # Relationship with Ticket
    ticket: Mapped["Ticket"] = relationship(
        back_populates="orders"
    )