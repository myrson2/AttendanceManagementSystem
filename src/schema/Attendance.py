from pydantic import BaseModel
from datetime import date, time

class AttendanceSchema(BaseModel):
    id: int
    student_id: int
    date: date
    status: str
    time_in: time | None = None
    time_out: time | None = None