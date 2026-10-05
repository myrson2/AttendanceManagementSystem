from src.models.Student import Student
from src.repository.repositories import StudentRepository
from src.schema.Student import StudentCreateSchema, StudentResponse


class StudentService:
    def __init__(self, repository: StudentRepository) -> None:
        self.repository = repository

    def create_student(self, student_data: StudentCreateSchema) -> StudentResponse:
        student = Student(**student_data.model_dump())
        saved_student = self.repository.create(student)
        return StudentResponse.model_validate(saved_student)
