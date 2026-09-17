# ask for number and print all of its factors
# Ask for a number and print all of its factors.

# Example:

# 12

# 1
# 2
# 3
# 4
# 6
# 12


number = int(input("Ener a number: "))
for divisor in range(1, number +1):
    if number % divisor == 0:
        print(divisor)