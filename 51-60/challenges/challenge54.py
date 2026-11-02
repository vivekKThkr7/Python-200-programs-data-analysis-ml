# Reverse an integer while keeping its sign.

number = int(input("Enter an integer: "))
sign = -1 if number < 0 else 1
number = abs(number)
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

reverse *= sign
print("Reversed number:", reverse)
