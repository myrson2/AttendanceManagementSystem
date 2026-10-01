from src.models.database import get_db


class AttendanceService:
    def __init__(self, attendance) -> None:
        self.attendance = attendance

    