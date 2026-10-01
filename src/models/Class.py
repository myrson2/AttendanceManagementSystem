from datetime import date, time
from sqlalchemy import Date, String, Time, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.database import Base

class Class(Base):
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


