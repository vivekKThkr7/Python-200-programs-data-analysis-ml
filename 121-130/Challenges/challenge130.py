# Build a safe calculator
# The Program should repeatedly ask: 

# Enter first number:
# Enter second number:
# Choose:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide

# Use try/except to handle invalid numeric input.

while True:

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        option = int(input("Choose an option: "))

        if option == 1:
            print("Sum:", num1 + num2)
            break

        elif option == 2:
            print("Subtract:", num1 - num2)
            break

        elif option == 3:
            print("Multiply:", num1 * num2)
            break

        elif option == 4:
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Divide:", num1 / num2)
                break

        else:
            print("Choose a valid option.")

    except ValueError:
        print("Please enter valid numbers.")