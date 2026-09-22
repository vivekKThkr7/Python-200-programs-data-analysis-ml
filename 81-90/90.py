students = [
    ["Ram", 75],
    ["Sita", 82],
    ["Hari", 35],
    ["Gita", 91]
]

for student in students:
    name = student[0]
    marks = student[1]

    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(name, "-", marks, "-", status)