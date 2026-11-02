# Create a file and write " First line "
# then run another program that uses "a" to add.

with open("notes.txt", "w") as file:
    file.write("First line\n")


with open("notes.txt", "a") as file:
    file.write("Second line\n")