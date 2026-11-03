from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class TeacherAssignment(Base):
    __tablename__ = "teacher_assignments"

    __table_args__ = (
        UniqueConstraint(
            "offering_id",
            "teacher_id",
            name="uq_teacher_assignment"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    offering_id: Mapped[int] = mapped_column(
        ForeignKey("course_offerings.id", ondelete="RESTRICT"),
        nullable=False
    )

    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="RESTRICT"),
        nullable=False
    )

    course_offering: Mapped["CourseOffering"] = relationship(
    back_populates="teacher_assignments"
    )

    teacher: Mapped["Teacher"] = relationship(
        back_populates="assignments"
    )

    schedules: Mapped[list["ClassSchedule"]] = relationship(
        back_populates="teacher_assignment"
    )