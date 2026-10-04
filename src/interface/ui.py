
from src.schema.Student import StudentCreateSchema


def created_student(): 
    student_data = {
            "student_number": input("Enter student number: ").strip(),
            "name": input("Enter student name: ").strip(),
            "email": input("Enter student email: ").strip(),
        }
    return StudentCreateSchema(**student_data)
    

def student_flow():
    # Create a user input for the student schema
    student = created_student()
    print(f"Student created: {student.model_dump()}")


def main():
    print('Starting the API server...')
    student_flow()


if '__main__' == __name__:
    main()