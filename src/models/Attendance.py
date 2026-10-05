from datetime import date, time
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if TYPE_CHECKING:
    from src.models.Class import ClassModel
    from src.models.Student import Student


class Attendance(Base):
    __tablename__ = "attendance"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
        nullable=False
    )

    class_id: Mapped[int] = mapped_column(
        ForeignKey("classes.id"),
        nullable=False
    )

    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    time_in: Mapped[time | None] = mapped_column(
        Time,
        nullable=True
    )

    time_out: Mapped[time | None] = mapped_column(
        Time,
        nullable=True
    )

    student: Mapped["Student"] = relationship(
        "Student",
        back_populates="attendance_records"
    )
    classes: Mapped["ClassModel"] = relationship(
        "ClassModel",
        back_populates="attendance_records"
    )