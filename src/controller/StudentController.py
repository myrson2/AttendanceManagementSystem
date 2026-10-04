from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from dependencies import get_student_service
from src.models.Student import Student
from src.schema.Student import StudentCreateSchema, StudentSchema
from src.service.StudentService import StudentService

router = APIRouter()

@router.post(
    "/students",
    response_model=StudentSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student_data: StudentCreateSchema,
    service: Annotated[StudentService, Depends(get_student_service)],
) -> Student:
    try:
        return service.create_student(student_data)
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this student number or email already exists.",
        ) from error