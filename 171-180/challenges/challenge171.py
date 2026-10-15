# Write a program than manage a foler and file.

# Requirements
# 1. Create a folder called data if it doesn't exist.
# 2. inside tghat folder, check for a file named employees.txt.
# 3. if the file already exists, print: Employee file already exists.
# 4. Otherwise, create the file and write Employee Records inside it.
# 5. Print: Employee file created. 


from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)

file_path = folder / "employees.txt"

if file_path.exists():
    print("Employee file already exists.")
else:
    file_path.write_text("Employee Records")
    print("Employee file created.")