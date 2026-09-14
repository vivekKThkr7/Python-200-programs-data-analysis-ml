# Factorial
n = int(input("Enter a number: "))
factorial = 1
for number in range(1, n+1):
    factorial *=number

print("Factorial: ", factorial)