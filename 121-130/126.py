# # append data

# ' w ' -> write : can replace the existing contents

with open("notes.txt", "w") as file:
    file.write("Hello\n")



# ' a ' -> append : add to the end 

with open("notes.txt", "a") as file:
    file.write("Python\n")

    