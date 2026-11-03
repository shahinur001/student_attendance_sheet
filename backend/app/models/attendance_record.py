from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    __table_args__ = (
        UniqueConstraint(
            "session_id",
            "student_id",
            name="uq_attendance_student"
        ),
        CheckConstraint(
            "status IN ('present', 'absent')",
            name="check_attendance_record_status"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    session_id: Mapped[int] = mapped_column(
        ForeignKey("attendance_sessions.id", ondelete="RESTRICT"),
        nullable=False
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="RESTRICT"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20), nullable=False
    )

    marked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    session: Mapped["AttendanceSession"] = relationship(
    back_populates="attendance_records"
    )

    student: Mapped["Student"] = relationship(
        back_populates="attendance_records"
    )

    audit_logs: Mapped[list["AttendanceAuditLog"]] = relationship(
        back_populates="attendance_record"
    )