# check wheather file exist. 

from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    print("File exist")

else:
    print("File does not exist.")
