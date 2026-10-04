from datetime import time

from sqlalchemy import String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Attendance import Attendance
from models.Enrollment import Enrollment
from src.models.database import Base


class ClassModel(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    room: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    day: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    start_time: Mapped[time] = mapped_column(
        Time,
        nullable=False
    )

    end_time: Mapped[time] = mapped_column(
        Time,
        nullable=False
    )

    enrollments: Mapped[list["Enrollment"]] = relationship(back_populates="class_")
    attendance_records: Mapped[list["Attendance"]] = relationship(back_populates="class_")

