from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from dependencies import get_student_repository
from src.models.Student import Student
from src.repository.repositories import StudentRepository
from src.schema.Student import StudentCreateSchema, StudentSchema

router = APIRouter()

@router.post(
    "/students",
    response_model=StudentSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student_data: StudentCreateSchema,
    repository: Annotated[StudentRepository, Depends(get_student_repository)],
) -> Student:
    student = Student(**student_data.model_dump())
    try:
        return repository.create(student)
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this student number or email already exists.",
        ) from error