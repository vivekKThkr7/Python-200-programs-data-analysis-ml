# Ask the user for the number using " int() "
# Use try/ecxceptso that entering text doesn't crash the program.

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number.")