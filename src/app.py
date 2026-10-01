from fastapi import FastAPI

from src.controller.StudentController import router as student_router
from src.models.database import create_tables

app = FastAPI()
app.include_router(student_router)


@app.on_event("startup")
def startup() -> None:
	create_tables()