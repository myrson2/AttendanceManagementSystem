from pydantic import BaseModel, ConfigDict

class StudentSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    student_number: str
    name: str
    email: str

class StudentCreateSchema(StudentSchema):
    pass

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_number: str
    name: str
