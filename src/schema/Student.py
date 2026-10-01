from pydantic import BaseModel, ConfigDict


class StudentCreateSchema(BaseModel):
    student_number: str
    name: str
    email: str

class StudentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    student_number: str
    name: str
    email: str
