# Ask for two numbers and report which is greater, or whether they are equal.

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if number1 > number2:
    print(number1, "is greater")
elif number2 > number1:
    print(number2, "is greater")
else:
    print("Both numbers are equal")
