# Given:  numbers = [1, 2, 3, 4, 5]
# Create 
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)
