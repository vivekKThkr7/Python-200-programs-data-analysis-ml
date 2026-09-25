# # create
# marks = {
#     "Ram": 75,
#     "Sita": 82,
#     "Hari": 35,
#     "Gita": 91
# }

# Ask the user for student's name and dispaly thir marks

marks = {
    "Ram": 75,
    "Sita": 82,
    "Hari": 35,
    "Gita": 91
}

name = input("Enter name of student: ")


if name in marks:
    print("Mark:", marks[name])
else:
    print("Invalid name!!!")