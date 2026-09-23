# Student Analyser with functions.

def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


def calculate_lowest(marks):
    lowest = marks[0]

    for mark in marks:
        if mark < lowest:
            lowest = mark

    return lowest


def count_passed(marks):
    passed = 0

    for mark in marks:
        if mark >= 40:
            passed += 1

    return passed


marks = [75, 82, 45, 91, 30]

total = calculate_total(marks)
average = total / len(marks)
highest = calculate_highest(marks)
lowest = calculate_lowest(marks)
passed = count_passed(marks)
failed = len(marks) - passed

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)