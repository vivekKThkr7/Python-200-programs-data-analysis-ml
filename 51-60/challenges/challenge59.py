# Find largest number
# # How many numbers? 5

# 10
# 25
# 7
# 50
# 30

# Largest: 50



largest = None

for i in range(5):
    number = int(input("Enter any number: "))

    if largest is None or number > largest:
        largest = number

print("Largest: ", largest)