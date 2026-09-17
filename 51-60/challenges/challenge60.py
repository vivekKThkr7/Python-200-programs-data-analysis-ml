# # Build a Number Analyzer.

# # Ask for one positive integer and display:

# # Number of digits
# # Sum of digits
# # Reversed number
# # Palindrome or not
# # Even or odd
# # Prime or not

# number = int(input("Enter a positive number: "))

# original = number
# digit_count = 0
# digit_sum = 0
# reverse = 0
# while number != 0:
#     digit = number % 10

#     digit_count += 1
#     digit_sum += digit
#     reverse = reverse * 10 + digit

#     number = number // 10

# print("Digits : ", digit_count)
# print("Sum of digits: ", digit_sum)
# print("reversed: ", reverse)

# if original == reverse:
#     print("Palindrome : True")
# else:
#     print("Palindrome: False")

# if original % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# if original < 2:
#     print("Prime: False")
# else:
#     is_Prime = True

#     for divisor in range(2, original):
#         if original % divisor == 0:
#             is_Prime = False
#             break

#     if is_Prime:
#         print("Prime: True")

#     else:
#         print("Prime: False")
        



number = int(input("Enter a positive number: "))

original = number
digit_count = 0
digit_sum = 0
reverse = 0

# Process digits
while number != 0:
    digit = number % 10

    digit_count += 1
    digit_sum += digit
    reverse = reverse * 10 + digit

    number = number // 10


# Display digit information AFTER the loop
print("Digits:", digit_count)
print("Sum of digits:", digit_sum)
print("Reversed:", reverse)


# Palindrome
if original == reverse:
    print("Palindrome: True")
else:
    print("Palindrome: False")


# Even / Odd
if original % 2 == 0:
    print("Even")
else:
    print("Odd")


# Prime
if original < 2:
    print("Prime: False")
else:
    is_prime = True

    for divisor in range(2, original):
        if original % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime: True")
    else:
        print("Prime: False")