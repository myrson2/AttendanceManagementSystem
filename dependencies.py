from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.models.database import get_db
from src.repository.repositories import (
	AttendanceRepository,
	ClassRepository,
	StudentRepository,
)
from src.service.StudentService import StudentService


# Repository dependency injection functions
def get_student_repository(
	db: Annotated[Session, Depends(get_db)],
) -> StudentRepository:
	return StudentRepository(db)


def get_class_repository(
	db: Annotated[Session, Depends(get_db)],
) -> ClassRepository:
	return ClassRepository(db)


def get_attendance_repository(
	db: Annotated[Session, Depends(get_db)],
) -> AttendanceRepository:
	return AttendanceRepository(db)


# Service dependency injection functions
def get_student_service(
	repository: Annotated[StudentRepository, Depends(get_student_repository)],
) -> StudentService:
	return StudentService(repository)
