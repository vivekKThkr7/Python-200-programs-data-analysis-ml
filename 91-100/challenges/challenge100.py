# Challenge 100 ⭐⭐⭐ — First Modular Program
# Build a Student Analyzer using functions.

# calculate_total()
# calculate_average()
# find_highest()
# find_lowest()
# count_passed()
# count_failed()


def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)


def find_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


def find_lowest(marks):
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


def count_failed(marks):
    failed = 0

    for mark in marks:
        if mark < 40:
            failed += 1

    return failed


marks = [75, 82, 45, 91, 30]

total = calculate_total(marks)
average = calculate_average(marks)
highest = find_highest(marks)
lowest = find_lowest(marks)
passed = count_passed(marks)
failed = count_failed(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)