# ASk for a number and count howmany digits it contains.
number = int(input("Enter a number: "))

count = 0

while number != 0:
    number = number // 10
    count += 1

print("Number of digits: ", count)
