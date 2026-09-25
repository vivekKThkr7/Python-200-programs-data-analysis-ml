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

if "Ram" in name:
    print("Mark : 75")

elif "Sita" in name:
    print("Mark : 82")

elif "Hari" in name:
    print("Mark : 35")

elif "Gita" in name: 
    print("Mark : 91")

else:
    print("Invalid name!!!")