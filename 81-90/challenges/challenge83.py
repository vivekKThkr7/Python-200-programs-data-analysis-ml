# Ask the user for a number and count how many times it appears.
numbers = [10, 20, 23, 25, 30, 40, 50]

user_input = int(input("Enter a number to count how many times it appears: "))

count = 0

for number in numbers:
    if number == user_input:
        count =+1

print(f"The number {user_input} appears {count} time(s) in the list.")