# Create an set of numbers. 
# Ask the user for number and check whether it exisits.

numbers = {10, 20, 30, 40, 50}

number = int(input("Enter a number: "))

if number in numbers:
    print("exists.")
else:
    print("Does not exist in set")