# Read a file

file = open("outputs/text/notes.txt", "r")

content = file.read()

file.close()

print(content)
