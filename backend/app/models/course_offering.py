from sqlalchemy import (
    String, 
    ForeignKey, 
    UniqueConstraint
) 
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class CourseOffering(Base):
    __tablename__ = "course_offerings"

    __table_args__ = (
        UniqueConstraint(
            "course_id",
            "term_id",
            "section",
            name="uq_course_offering"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id", ondelete="RESTRICT"),
        nullable=False
    )

    term_id: Mapped[int] = mapped_column(
        ForeignKey("academic_terms.id", ondelete="RESTRICT"),
        nullable=False
    )

    section: Mapped[str] = mapped_column(
        String(20), nullable=False, default="A"
    )

    course: Mapped["Course"] = relationship(
    back_populates="course_offerings"
    )

    academic_term: Mapped["AcademicTerm"] = relationship(
        back_populates="course_offerings"
    )

    teacher_assignments: Mapped[list["TeacherAssignment"]] = relationship(
        back_populates="course_offering"
    )

    enrollments: Mapped[list["CourseEnrollment"]] = relationship(
        back_populates="course_offering"
    )

    schedules: Mapped[list["ClassSchedule"]] = relationship(
        back_populates="course_offering"
    )