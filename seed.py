from datetime import time

from sqlalchemy.orm import Session

from src.models.Class import ClassModel
from src.models.database import get_db


def seed_classes(db: Session):
    class_names = ["Math", "Science", "English", "History"]
    classes_to_insert = []
    
    start_hour = 12
    
    for name in class_names:
        end_hour = start_hour + 2
        
        new_class = ClassModel(
            name=name,
            room="Room 101",
            day="Monday",
            start_time=time(hour=start_hour, minute=0),
            end_time=time(hour=end_hour, minute=0)
        )
        classes_to_insert.append(new_class)
        start_hour = end_hour

    db.add_all(classes_to_insert)
    db.commit()

    print(f"Successfully inserted {len(classes_to_insert)} classes!")

if __name__ == "__main__":
    db_session = next(get_db())
    try:
        seed_classes(db_session)
    finally:
        db_session.close()
