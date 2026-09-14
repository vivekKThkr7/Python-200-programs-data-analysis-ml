# Mini Number Analyzer
# Ask the user for a positive integer.

# Then calculate:

# number of digits
# sum of digits
# reversed number
# whether it is a palindrome

# number = int(input("Enter a positive number: "))

# original = number
# digit_count = 0
# digit_sum = 0
# reverse = 0

# while number != 0:
#     digit = number % 10

#     digit_count +=1
#     digit_sum += digit
#     reverse = reverse * 10 * digit

#     number = number // 10

#     print("Digits: ", digit_count)
#     print("Sum of digits: ", digit_sum)
#     print("Reversed: ", reverse)

#     if original == reverse:
#         print("Palindrome: True")
#     else:
#         print("Palindrome: False")




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

print("Digits:", digit_count)
print("Sum of digits:", digit_sum)
print("Reversed:", reverse)

if original == reverse:
    print("Palindrome: True")
else:
    print("Palindrome: False")