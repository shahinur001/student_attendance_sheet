from datetime import date

from sqlalchemy import String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class AcademicTerm(Base):
    __tablename__ = "academic_terms"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    academic_year: Mapped[str] = mapped_column(
        String(20), nullable=False
    )

    start_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    end_date: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    course_offerings: Mapped[list["CourseOffering"]] = relationship(
        back_populates="academic_term"
    )