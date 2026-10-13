# Our file realistic prgogram

from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    print("File already exists.")
else:
    file_path.write_text("Python Developer Notes\n", encoding="utf-8")
    print("File created.")
    