# Save user Input

name = input("Enter your name: ")

with open("outputs/text/names.txt", "a") as file:
    file.write(name + "\n")

print("Name saved successfully.")
