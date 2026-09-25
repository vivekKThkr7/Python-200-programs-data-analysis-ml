# Student Dictionary Analyzer

marks = {
    "Ram": 75,
    "Sita": 82,
    "Hari": 35,
    "Gita": 91,
    "Mohan": 48
}

total = 0
passed = 0
failed = 0

highest = None
highest_student = None

for name, mark in marks.items():
    total += mark

    if mark >= 40:
        passed += 1
    else:
        failed += 1

    if highest is None or mark > highest:
        highest = mark
        highest_student = name

average = total / len(marks)

print("Total students:", len(marks))
print("Total marks:", total)
print("Average:", average)
print("Passed:", passed)
print("Failed:", failed)
print("Highest mark:", highest)
print("Highest student:", highest_student)