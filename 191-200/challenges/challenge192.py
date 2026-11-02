# NumPy calculations and statistics.
# Create a NumPy array and calculate the total, mean, median, highest mark, lowest mark, and standard deviation.

import numpy as np

marks = np.array([65, 70, 85, 90, 95])

print("Total: ", np.sum(marks))
print("Mean: ", np.mean(marks))
print("medium: ", np.median(marks))
print("Highest mark: ", np.max(marks))
print("Lowest mark: ", np.min(marks))
print("Standard Deviation: ", np.std(marks))

