from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"

    __table_args__ = (
        UniqueConstraint(
            "offering_id",
            "student_id",
            name="uq_course_enrollment"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    offering_id: Mapped[int] = mapped_column(
        ForeignKey("course_offerings.id", ondelete="RESTRICT"),
        nullable=False
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="RESTRICT"),
        nullable=False
    )

    course_offering: Mapped["CourseOffering"] = relationship(
        back_populates="enrollments"
    )

    student: Mapped["Student"] = relationship(
        back_populates="enrollments"
    )