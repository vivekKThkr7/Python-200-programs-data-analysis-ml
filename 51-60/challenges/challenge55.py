# Check whether a non-negative integer is a palindrome.
# Negative integers are not palindromes because of the minus sign.

number = int(input("Enter an integer: "))

if number < 0:
    print("Not a palindrome")
else:
    original = number
    working_number = number
    reverse = 0

    while working_number > 0:
        digit = working_number % 10
        reverse = reverse * 10 + digit
        working_number //= 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not a palindrome")
