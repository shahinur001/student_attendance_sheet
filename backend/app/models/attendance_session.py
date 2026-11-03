from datetime import date, datetime

from sqlalchemy import (
    Date,
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AttendanceSession(Base):
    __tablename__ = "attendance_sessions"

    __table_args__ = (
        UniqueConstraint(
            "schedule_id",
            "class_date",
            name="uq_attendance_schedule_date"
        ),
        CheckConstraint(
            "status IN ('draft', 'submitted', 'cancelled')",
            name="check_attendance_session_status"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    schedule_id: Mapped[int] = mapped_column(
        ForeignKey("class_schedules.id", ondelete="RESTRICT"),
        nullable=False
    )

    class_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20), default="draft", nullable=False
    )

    submitted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )