# Employee CSV System.
# ceate a program that stores employee records in a file (outputs/csv/employees.csv)
# Employee msut contains; name, role, salary
# requirements:
# 1. Create at least three employee records. 
# 2. Write the records into outputs/csv/employees.csv
# 3. include column headings.
# read the records back from the same file.
# Display each employee's name, role, salary.


# Explore csv.DictWriter, writeheader(), writerows(), and csv.DictReader.


import csv

employees = [
    {"name": "Ram", "role": "Developer", "salary": 2500},
    {"name": "Sita", "role": "Designer", "salary": 2800},
    {"name": "Hari", "role": "Tester", "salary": 2300},
]

# Write records with column headings
with open("outputs/csv/employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "role", "salary"])
    writer.writeheader()
    writer.writerows(employees)

# Read the records back
with open("outputs/csv/employees.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        salary = int(row["salary"])  # CSV values are strings
        print(f"{row['name']} - {row['role']} - {salary}")