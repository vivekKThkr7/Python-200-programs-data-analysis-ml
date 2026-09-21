# Seach with " in "

numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number: "))

found = False

for number in numbers:
    if number == search:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")