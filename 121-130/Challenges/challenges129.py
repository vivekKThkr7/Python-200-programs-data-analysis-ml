# Ask the user for two numbers.

# handle invalid input using try/except

# Then print their sum

try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    print("Sum : ", num1+num2)
    

except ValueError:
    print("Please enter a valid number.")