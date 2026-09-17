# Build a Number Analyzer.

# Ask for one positive integer and display:

# Number of digits
# Sum of digits
# Reversed number
# Palindrome or not
# Even or odd
# Prime or not

number = int(input("Enter a positive number: "))

original = number
digit_count = 0
digit_sum = 0
reverse = 0
while number != 0:
    digit = number % 10

    digit_count += 1
    digit_sum += digit
    reverse = reverse * 10 + digit

    number = number // 10
    print("Digits : ", digit_count)
    print("Sum of digits: ", digit_sum)
    print("reversed: ", reverse)

    if original == reverse:
        print("Palindrome : True")
    else:
        print("Not Palindrome")

    if original % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if number < 2:
        print("Not Prime")
else:
    is_Prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_Prime = False
            break

    if is_Prime:
        print("Prime")

    else:
        print("Not Prime")
        