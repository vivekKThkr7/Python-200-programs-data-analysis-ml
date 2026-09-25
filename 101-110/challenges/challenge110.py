# # Build a student Dictionary Analyzer
# # students = {
# #     "Ram": 75,
# #     "Sita": 82,
# #     "Hari": 35,
# #     "Gita": 91,
# #     "Mohan": 48
# # }
# # Your program should calcualte 
# # Total students
# # Total marks
# # Average
# # Highest mark
# # Lowest mark
# # Passed
# # Failed

# # Also find 
# Student with highest mark
# Student with lowest mark

# For the main calculations, don't use:
# sum()
# max()
# min()


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
lowest = None

highest_student = None
lowest_student = None

for name, mark in marks.items():

    total += mark

    if mark >= 40:
        passed += 1
    else:
        failed += 1

    if highest is None or mark > highest:
        highest = mark
        highest_student = name

    if lowest is None or mark < lowest:
        lowest = mark
        lowest_student = name


average = total / len(marks)

print("Total students:", len(marks))
print("Total marks:", total)
print("Average:", average)
print("Highest mark:", highest)
print("Highest student:", highest_student)
print("Lowest mark:", lowest)
print("Lowest student:", lowest_student)
print("Passed:", passed)
print("Failed:", failed)