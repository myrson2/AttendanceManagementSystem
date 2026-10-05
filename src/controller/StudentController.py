from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from dependencies import (
    create_access_token,
    get_current_user,
    get_jwt_secret_key,
    get_student_service,
)
from src.models.Student import StudentModel
from src.schema.Student import (
    StudentCreatedResponse,
    StudentCreateSchema,
    StudentResponse,
)
from src.service.StudentService import StudentService

router = APIRouter()

@router.post(
    "/students",
    response_model=StudentCreatedResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(
    student_data: StudentCreateSchema,
    service: Annotated[StudentService, Depends(get_student_service)],
    secret_key: Annotated[str, Depends(get_jwt_secret_key)],
) -> StudentCreatedResponse:
    """Create a student, then return their details with a signed access token."""
    try:
        student = service.create_student(student_data)
        return StudentCreatedResponse(
            **student.model_dump(),
            access_token=create_access_token(student.id, secret_key),
        )
    except IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A student with this student number or email already exists.",
        ) from error


@router.get("/students/me", response_model=StudentResponse)
def read_current_student(
    current_user: Annotated[StudentModel, Depends(get_current_user)],
) -> StudentResponse:
    """Return the student resolved from the request's validated bearer token."""
    return StudentResponse.model_validate(current_user)