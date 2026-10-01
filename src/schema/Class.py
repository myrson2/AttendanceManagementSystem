from datetime import date, time
from pydantic import BaseModel

class ClassSchema(BaseModel):
    id: int
    name: str
    room: str
    day: str
    start_time: time
    end_time: time