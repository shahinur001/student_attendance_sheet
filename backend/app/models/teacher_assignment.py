from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

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