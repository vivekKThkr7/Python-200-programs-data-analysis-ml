# Filter passing marks

marks = [35, 80, 42, 27, 91, 55]

passed_marks = []

for mark in marks:
    if mark >= 40:
        passed_marks.append(mark)

print("Passing marks: ", passed_marks)