def show_message():
    message = "Hello from inside the function"
    print(message)

show_message()

try:
    print(message)
except NameError as error:
    print("Error:", error)
    print("The variable 'message' is local to the function.")
