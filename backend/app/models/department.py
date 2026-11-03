from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )

    teachers: Mapped[list["Teacher"]] = relationship(
        back_populates="department"
    )

    students: Mapped[list["Student"]] = relationship(
        back_populates="department"
    )

    courses: Mapped[list["Course"]] = relationship(
        back_populates="department"
    )   