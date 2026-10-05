from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from config import settings
from src.models.database import get_db
from src.models.Student import StudentModel
from src.repository.repositories import (
	AttendanceRepository,
	ClassRepository,
	StudentRepository,
)
from src.service.StudentService import StudentService

bearer_scheme = HTTPBearer(auto_error=False)


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


def get_jwt_secret_key() -> str:
	"""Return the signing secret, or fail closed if JWT auth is not configured."""
	secret_key = settings.JWT_SECRET_KEY
	if secret_key is None or len(secret_key) < 32:
		raise HTTPException(
			status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
			detail="JWT authentication is not configured.",
		)
	return secret_key

def create_access_token(student_id: int, secret_key: str) -> str:
	"""Sign a 30-minute HS256 token whose subject identifies the student."""
	now = datetime.now(timezone.utc)
	return jwt.encode(
		{
			"sub": str(student_id),
			"iat": now,
			"exp": now + timedelta(minutes=30),
		},
		secret_key,
		algorithm="HS256",
	)


def get_current_user(
	credentials: Annotated[
		HTTPAuthorizationCredentials | None,
		Depends(bearer_scheme),
	],
	repository: Annotated[StudentRepository, Depends(get_student_repository)],
	secret_key: Annotated[str, Depends(get_jwt_secret_key)],
) -> StudentModel:
	"""Validate the bearer token and load its student for the requesting endpoint.

	The token's signature and expiry are checked before its subject is used as
	the student ID. Missing, invalid, expired, or unknown-student tokens return
	401; a valid token returns the corresponding student model.
	"""
	unauthorized = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Invalid or missing access token.",
		headers={"WWW-Authenticate": "Bearer"},
	)
	if credentials is None:
		raise unauthorized

	try:
		payload = jwt.decode(
			credentials.credentials,
			secret_key,
			algorithms=["HS256"],
		)
	except jwt.InvalidTokenError as error:
		raise unauthorized from error

	subject = payload.get("sub")
	if not isinstance(subject, str) or not subject.isascii() or not subject.isdecimal():
		raise unauthorized

	try:
		student = repository.get(int(subject))
	except (ValueError, OverflowError) as error:
		raise unauthorized from error

	if student is None:
		raise unauthorized
	return student
