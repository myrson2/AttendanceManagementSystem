from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if TYPE_CHECKING:
    from src.models.Attendance import Attendance
    from src.models.Enrollment import Enrollment


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    enrollments: Mapped[list["Enrollment"]] = relationship(
        "Enrollment",
        back_populates="student"
    )
    attendance_records: Mapped[list["Attendance"]] = relationship(
        "Attendance",
        back_populates="student"
    )