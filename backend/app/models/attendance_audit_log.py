from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AttendanceAuditLog(Base):
    __tablename__ = "attendance_audit_logs"

    __table_args__ = (
        CheckConstraint(
            "old_status IS NULL OR old_status IN ('present', 'absent')",
            name="check_audit_old_status"
        ),
        CheckConstraint(
            "new_status IN ('present', 'absent')",
            name="check_audit_new_status"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    attendance_record_id: Mapped[int] = mapped_column(
        ForeignKey("attendance_records.id", ondelete="RESTRICT"),
        nullable=False
    )

    changed_by: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False
    )

    old_status: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )

    new_status: Mapped[str] = mapped_column(
        String(20), nullable=False
    )

    changed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    reason: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )