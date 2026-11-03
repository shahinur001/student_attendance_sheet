from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    department_id: Mapped[int | None] = mapped_column(
        ForeignKey("departments.id", ondelete="SET NULL"),
        nullable=True
    )

    employee_id: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )

    designation: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )

    user: Mapped["User"] = relationship(
    back_populates="teacher"
    )

    department: Mapped["Department | None"] = relationship(
        back_populates="teachers"
    )

    assignments: Mapped[list["TeacherAssignment"]] = relationship(
        back_populates="teacher"
    )