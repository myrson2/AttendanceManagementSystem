from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Class import ClassModel
from models.Student import Student
from src.models.database import Base


class Enrollment(Base):
    __tablename__ = "enrollment"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), nullable=False)

    student: Mapped["Student"] = relationship(back_populates="enrollments")
    class_: Mapped["ClassModel"] = relationship(back_populates="enrollments")