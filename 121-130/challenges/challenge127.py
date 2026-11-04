# Ask the user for thier name and save it to: names.txt
# use append mode.


name = input("Enter your name: ")
with open("outputs/text/names.txt", "a")as file:
    file.write(name + "\n")

print("Name saved")

