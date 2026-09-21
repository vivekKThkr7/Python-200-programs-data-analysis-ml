# 1. Ask how many students
# 2. Enter each student's marks
# 3. Store all marks in a list
# 4. Display the list
# 5. Calculate total
# 6. Calculate average
# 7. Find highest
# 8. Find lowest
# 9. Count passed
# 10. Count failed

# Restriction:
# Don't use sum(), max(), min()

students = int(input("How many Students? "))

marks = []

# Get marks and store them in the list.
for i in range(students):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

print("Marks: ", marks)

# total
total = 0
for mark in marks:
    total += mark


# Average
average = total / len(marks)

# Highest and lowest
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark


# Passed or failed
passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed +=1

    else:
        failed +=1

print("Total: ", total)
print("Average: ", average)
print("Highest: ", highest)
print("Lowest: ", lowest)
print("Passed: ", passed)
print("Failed: ", failed)
