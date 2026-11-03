from datetime import datetime

from sqlalchemy import String, Boolean, DateTime, CheckConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'teacher', 'student')",
            name="check_user_role"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(20), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
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

    teacher: Mapped["Teacher"] = relationship(
        back_populates="user",
        uselist=False
    )

    student: Mapped["Student"] = relationship(
    back_populates="user",
    uselist=False
    )

    attendance_changes: Mapped[list["AttendanceAuditLog"]] = relationship(
    back_populates="changed_by_user",
    foreign_keys="AttendanceAuditLog.changed_by"
    )