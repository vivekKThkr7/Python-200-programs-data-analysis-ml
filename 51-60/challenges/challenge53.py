# Ask for an integer and count its digits. The minus sign is not counted.

number = abs(int(input("Enter an integer: ")))
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number //= 10
        count += 1

print("Number of digits:", count)
