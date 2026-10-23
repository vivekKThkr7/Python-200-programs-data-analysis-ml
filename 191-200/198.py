# Understanding maching learning and Spitting Data

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()   # loads the sample dataset

X = iris.data
y = iris.target  # seperates tghe measurements from the class labels.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,   # means 20% of the samples are assigned to the test set. 
    random_state=42,  # makes the random split reproducible.
    stratify=y  # helps preserve tge distribution of target classes across the two subsets.
)    # splits both the features and thier corresponding lables into matching training and testing. 

print("Total samples:", len(X))
print("Number of features:", X.shape[1])

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("Training labels:", len(y_train))
print("Testing labels:", len(y_test))




# Here we haven't trained a model yet. we're preparing the data so that the next program can train and evaluate one correctly. 

