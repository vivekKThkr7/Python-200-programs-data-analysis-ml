# Using the same dictionary. Print every students:
# name
# marks
# pass or fail


marks = {
    "Ram": 75,
    "Sita": 82,
    "Hari": 35,
    "Gita": 91
}

for name, mark in marks.items():
    if mark >= 40:
        print(name, mark, " -> pass")
    else:
        print(name, mark, "-> Fail")