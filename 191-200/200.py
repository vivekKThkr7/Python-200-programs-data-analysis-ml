# Final Capstone: Data Analysis and AI Pipeline

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# 1. Load the dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = [
    iris.target_names[index]
    for index in iris.target
]

# 2. Explore the data
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isna().sum())

print("\nExact duplicate rows:")
print(df.duplicated().sum())

# For this exercise, remove missing rows and exact duplicates.
# In real work, confirm that duplicates are erroneous records
# before removing them; repeated measurements can be legitimate.
df = df.dropna().drop_duplicates().reset_index(drop=True)

# 3. Analyze by flower species
print("\nAverage measurements by species:")
print(
    df.groupby("species")[iris.feature_names]
    .mean()
    .round(2)
)

# 4. Visualize two measurements
x_feature = "sepal length (cm)"
y_feature = "petal length (cm)"

for species in iris.target_names:
    subset = df[df["species"] == species]

    plt.scatter(
        subset[x_feature],
        subset[y_feature],
        label=species
    )

plt.xlabel(x_feature)
plt.ylabel(y_feature)
plt.title("Iris Flower Measurements")
plt.legend()
plt.tight_layout()
plt.show()

# 5. Separate features and labels
X = df[iris.feature_names]
y = df["species"]

# 6. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 7. Create and train the model
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

model.fit(X_train, y_train)

# 8. Make predictions
y_pred = model.predict(X_test)

# 9. Evaluate the model
print("\nModel accuracy:")
print(round(accuracy_score(y_test, y_pred), 3))

print("\nConfusion matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred,
        labels=list(iris.target_names)
    )
)

print("\nClassification report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=list(iris.target_names),
        target_names=list(iris.target_names),
        zero_division=0
    )
)

# 10. Inspect a prediction for one test example
sample = X_test.iloc[[0]]

predicted_species = model.predict(sample)[0]
actual_species = y_test.iloc[0]

print("\nExample prediction:")
print("Actual species:", actual_species)
print("Predicted species:", predicted_species)