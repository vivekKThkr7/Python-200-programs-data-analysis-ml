# Return if number is even or not.

def check_even(number):
    if number % 2 == 0:
        return "True"
    else:
        return False


result1 = check_even(23)
result2 = check_even(10)

print(result1)
print(result2)