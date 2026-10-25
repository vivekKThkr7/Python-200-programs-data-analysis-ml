# NumPy arrays
# Create a NumPy array: [12, 13, 25, 30, 45]

# Program must display the original array, add 5 to each element, multiply each by 2, calculate the sum and mean and print the first and last elements.

import numpy as np

numbers = np.array([12, 18, 25, 30, 45])

print("Original: ", numbers)
print("Plus 5: ", numbers + 5)
print("Times 2: ", numbers * 2)
print("Sum: ", numbers.sum())
print("Mean: ", numbers.mean())
print("First element: ", numbers[0])
print("Last element: ", numbers[-1])


