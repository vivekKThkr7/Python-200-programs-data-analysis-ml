# understanding machine learning and splitting data. Prepare the Iris dataset correctly. 
# using load_iris() and train_test_split():
# 1. Seperate X and y
# 2. Use 20% of the data for testing
# 3. Set random_state = 42
# 4. Usie stratify = y
# 5. Print the number of training and testing samples. 
# 6. print their features shapes and label length. 
# 7. Verify that every class appears in both sets. 

# Hint: use X.shape, X_train.shape, X_test.shape, len(y_train) and np.unique(..., return_count=True)


import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y, = iris.data, iris.target   # X = measurements, y = species

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Total samples:", X.shape[0])   # 150
print("Number of features:", X.shape[1])   # 4
print("Training samples:", X_train.shape[0]) # 120
print("Testing samples:", X_test.shape[0])  # 30
print("X_train shape:", X_train.shape, "| y_train length:", len(y_train))
print("X_test shape:", X_test.shape, "| y_test length:", len(y_test))\


# Verify every class appears in both sets
classes, counts = np.unique(y_train, return_counts=True)
print("Train classes:", classes.tolist(), "counts:", counts.tolist())
classes, counts = np.unique(y_test, return_counts=True)
print("Test classes:", classes.tolist(), "counts:", counts.tolist())
 