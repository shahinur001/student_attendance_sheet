from sqlalchemy import (
    String, 
    ForeignKey, 
    UniqueConstraint
) 
from sqlalchemy.orm import Mapped, mapped_column

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