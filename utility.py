import uuid
from datetime import datetime

def generate_id() -> str:
    date_str = datetime.utcnow().strftime("%Y%m%d")
    random_suffix = uuid.uuid4().hex[:6].upper()
    return f"{date_str}-{random_suffix}"