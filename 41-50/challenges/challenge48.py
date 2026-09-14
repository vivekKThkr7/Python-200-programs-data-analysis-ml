n = int(input("Enter a number: "))
# n = int(input("Enter n: "))

total = 0

for number in range(1, n + 1):
    total += number

print("Sum =", total)