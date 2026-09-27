# Save user Input

name = input("Enter your name: ")

with open("names.txt", "a") as file:
    file.write(name + "\n")

print("Name saved successfully.")
