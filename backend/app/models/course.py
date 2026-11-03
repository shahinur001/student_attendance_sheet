from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id", ondelete="RESTRICT"),
        nullable=False
    )

    course_code: Mapped[str] = mapped_column(
        String(30), unique=True, nullable=False
    )

    course_name: Mapped[str] = mapped_column(
        String(200), nullable=False
    )

    credit: Mapped[float] = mapped_column(
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )

    department: Mapped["Department"] = relationship(
    back_populates="courses"
    )

    course_offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="course"
    )