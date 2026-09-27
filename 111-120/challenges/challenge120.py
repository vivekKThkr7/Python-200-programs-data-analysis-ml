# # Challenge 120 ⭐⭐⭐

# Build a Duplicate Analyzer.

# Ask the user to enter 5 numbers.

# Store them in a list.

# Then display:

# Original numbers: [...]
# Unique numbers: {...}
# Total numbers: 5
# Unique numbers: 4
# Duplicates found: Yes
# Example

# Input:

# 10
# 20
# 10
# 30
# 20

# Output:

# Original numbers: [10, 20, 10, 30, 20]
# Unique numbers: {10, 20, 30}
# Total numbers: 5
# Unique numbers: 3
# Duplicates found: Yes

numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

unique_numbers = set(numbers)

print("Original numbers:", numbers)
print("Unique numbers:", unique_numbers)
print("Total numbers:", len(numbers))
print("Unique numbers:", len(unique_numbers))

if len(numbers) == len(unique_numbers):
    print("Duplicates found: No")
else:
    print("Duplicates found: Yes")