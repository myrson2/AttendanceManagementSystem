from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models.Attendance import Attendance
from src.models.Class import ClassModel
from src.models.database import Base
from src.models.Student import Student

ModelT = TypeVar("ModelT", bound=Base)

class BaseRepository[ModelT: Base]:
    def __init__(self, db: Session, model: type[ModelT]) -> None:
        self.db = db
        self.model = model

    def get(self, entity_id: int) -> ModelT | None:
        return self.db.get(self.model, entity_id)

    def list_all(self) -> list[ModelT]:
        return list(self.db.scalars(select(self.model)).all())

    def create(self, entity: ModelT) -> ModelT:
        self.db.add(entity)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        self.db.refresh(entity)
        return entity

    def delete(self, entity_id: int) -> bool:
        entity = self.get(entity_id)
        if entity is None:
            return False

        self.db.delete(entity)
        self.db.commit()
        return True

class StudentRepository(BaseRepository[Student]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, Student)

    def update(self, student_id: int, updated_student: Student) -> Student | None:
        existing_student = self.get(student_id)
        if existing_student is None:
            return None

        for attr, value in vars(updated_student).items():
            if attr != "id" and value is not None:
                setattr(existing_student, attr, value)

        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise
        self.db.refresh(existing_student)
        return existing_student

class ClassRepository(BaseRepository[ClassModel]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, ClassModel)

class AttendanceRepository(BaseRepository[Attendance]):
    def __init__(self, db: Session) -> None:
        super().__init__(db, Attendance)