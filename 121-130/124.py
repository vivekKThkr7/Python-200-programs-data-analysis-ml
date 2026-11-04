# Read multiple lines

file = open("outputs/text/students.txt", "r")

for line in file:
    print(line.strip())

file.close()