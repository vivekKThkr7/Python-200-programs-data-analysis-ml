# Create a function with a local variable. try accessing that variable outside the function.
# Observe the error and understand scope.




def show_message():
    message = "Hello from inside the function"
    print(message)

show_message()

try:
    print(message)
except NameError as error:
    print("Error:", error)
    print("The variable 'message' is local to the function.")

# # output
# Hello from inside the function
# Error: name 'message' is not defined
# The variable 'message' is local to the function.