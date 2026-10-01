from datetime import date, time
from sqlalchemy import Date, String, Time, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id"),
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