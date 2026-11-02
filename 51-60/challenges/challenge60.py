# Build a Number Analyzer for one positive integer.
# Display its digit count, digit sum, reverse, palindrome status, parity, and primality.

from math import isqrt

while True:
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if number > 0:
        break

    print("The number must be greater than zero.")

original = number
working_number = number
digit_count = 0
digit_sum = 0
reverse = 0

while working_number > 0:
    digit = working_number % 10
    digit_count += 1
    digit_sum += digit
    reverse = reverse * 10 + digit
    working_number //= 10

print("Digits:", digit_count)
print("Sum of digits:", digit_sum)
print("Reversed:", reverse)
print("Palindrome:", original == reverse)
print("Even" if original % 2 == 0 else "Odd")

is_prime = True
if original < 2:
    is_prime = False
else:
    for divisor in range(2, isqrt(original) + 1):
        if original % divisor == 0:
            is_prime = False
            break

print("Prime:", is_prime)
