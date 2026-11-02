# Ask for a positive integer and print all of its positive factors.

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            print(divisor)
