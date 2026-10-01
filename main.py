
import sys
from pathlib import Path
import uvicorn
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent / "src"))
load_dotenv()

def start_api_server() -> None:
    uvicorn.run("src.app:app", host="127.0.0.1", port=8010, log_level="info")

if __name__ == "__main__":
    start_api_server()

