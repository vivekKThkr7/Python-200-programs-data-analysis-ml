
# Create two new list passed and failed

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 99]

passed_marks = []
failed_marks = []

for mark in marks:
    if mark < 40:
        failed_marks.append(mark)
        

    else:
        passed_marks.append(mark)
        

print("Failed Marks: ", failed_marks)
print("Passed marks: ", passed_marks)
