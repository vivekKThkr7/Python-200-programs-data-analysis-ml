# Find passed students

marks = {
    "Ram" : 30,
    "hari" : 45,
    "Gita" : 90,
    "Sita" : 56
}

for name, mark in marks.items():
    if mark >= 40:
        print(name, " -> pass")
    else:
        print(name, "-> Fail")