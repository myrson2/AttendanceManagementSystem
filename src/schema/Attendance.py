from pydantic import BaseModel, Field
from datetime import date, time
from utility import generate_id

def generate_attendance_id() -> str:
    return f"ATD-{generate_id()}"

class AttendanceSchema(BaseModel):
    attendance_id: str = Field(default_factory=generate_id)
    student_id: int
    date: date
    status: str
    time_in: time | None = None
    time_out: time | None = None