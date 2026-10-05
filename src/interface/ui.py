
from src.schema.Student import StudentCreateSchema
import httpx

def created_student(): 
    student_data = {
            "student_number": input("Enter student number: ").strip(),
            "name": input("Enter student name: ").strip(),
            "email": input("Enter student email: ").strip(),
        }
    return StudentCreateSchema(**student_data)
    

def student_flow():
    student = created_student()

    response = httpx.post(
        "http://127.0.0.1:8010/students",
        json=student.model_dump(),
        timeout=10.0,
    )
    response.raise_for_status()
    print(f"Student created: {response.json()}")


def main():
    print('Starting the API server...')
    student_flow()


if '__main__' == __name__:
    main()