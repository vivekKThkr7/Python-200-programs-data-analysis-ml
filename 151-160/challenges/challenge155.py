# Create a global variable and a local variable with the same name
# print both and observe the difference

name = "Global Name"

def show_name():
    name = "Local Name"
    print("Inside function:", name)

print("Outside function:", name)
show_name()
