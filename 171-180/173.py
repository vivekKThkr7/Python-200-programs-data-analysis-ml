# Create a file
# pathlib can also create a file.

from pathlib import Path

file_path = Path("notes.txt")

file_path.write_text("Hell Python", encoding="utf-8")

print("File Created.")
