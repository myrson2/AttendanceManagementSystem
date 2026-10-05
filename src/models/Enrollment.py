from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.database import Base

if TYPE_CHECKING:
    from src.models.Class import ClassModel
    from src.models.Student import StudentModel


class EnrollmentModel(Base):
    __tablename__ = "enrollment"

    id: Mapped[int] = mapped_column(primary_key=True)

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)

    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"), nullable=False)

    student: Mapped["StudentModel"] = relationship(
        "StudentModel",
        back_populates="enrollments"
    )
    classes: Mapped["ClassModel"] = relationship(
        "ClassModel",
        back_populates="enrollments"
    )