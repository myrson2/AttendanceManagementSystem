from datetime import date, time
from sqlalchemy import Date, String, Time, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.database import Base

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