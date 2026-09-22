students = [
    ["Ram", 75],
    ["Sita", 80],
    ["Hari", 85],
    ["Gita", 75],
    ["Mohan", 40]
]

print("Student Records")
print("--------------------")

total = 0
passed = 0
failed = 0

highest = students[0][1]
lowest = students[0][1]

for student in students:
    name = student[0]
    mark = student[1]

    total += mark

    if mark >= 40:
        status = "Pass"
        passed += 1
    else:
        status = "Fail"
        failed += 1

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    print(name, "-", mark, "-", status)

average = total / len(students)

print()
print("Total students:", len(students))
print("Passed:", passed)
print("Failed:", failed)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average:", average)