name = "Global Name"

def show_name():
    name = "Local Name"
    print("Inside function:", name)

print("Outside function:", name)
show_name()
