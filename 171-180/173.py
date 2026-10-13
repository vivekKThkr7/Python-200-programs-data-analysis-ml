# # Create a file
# # pathlib can also create a file.

# from pathlib import Path

# file_path = Path("notes.txt")

# file_path.write_text("Hell Python", encoding="utf-8")

# print("File Created.")





# Reading and writing CVS Files - Comma-Seperated Values
# Examples
# name,role,salary
# Ram,Developer,2500
# Sita,Designer,2800


import csv

employees = [
    {"name": "Ram", "role": "Developer", "salary": 2500},
    {"name": "Sita", "role": "Designer", "salary": 2800},
]

# Write employee data to a CSV file
with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "role", "salary"]
    )

    writer.writeheader()
    writer.writerows(employees)

# Read employee data from the CSV file
with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        print(
            f"{employee['name']} - "
            f"{employee['role']} - "
            f"{employee['salary']}"
        )