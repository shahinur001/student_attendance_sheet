from datetime import time

from sqlalchemy import (
    Integer,
    String,
    Time,
    ForeignKey,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class ClassSchedule(Base):
    __tablename__ = "class_schedules"

    __table_args__ = (
        CheckConstraint(
            "day_of_week BETWEEN 0 AND 6",
            name="check_schedule_day"
        ),
        CheckConstraint(
            "end_time > start_time",
            name="check_schedule_time"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    offering_id: Mapped[int] = mapped_column(
        ForeignKey("course_offerings.id", ondelete="RESTRICT"),
        nullable=False
    )

    teacher_assignment_id: Mapped[int] = mapped_column(
        ForeignKey("teacher_assignments.id", ondelete="RESTRICT"),
        nullable=False
    )

    day_of_week: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    start_time: Mapped[time] = mapped_column(
        Time, nullable=False
    )

    end_time: Mapped[time] = mapped_column(
        Time, nullable=False
    )

    room: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )