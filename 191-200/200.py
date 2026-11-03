# Final Capstone: Data Analysis and Machine Learning with the Wine Dataset

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# 1-2. Load the Wine dataset and create a DataFrame
wine = load_wine()

feature_names = list(wine.feature_names)
class_names = list(wine.target_names)
class_labels = list(range(len(class_names)))

df = pd.DataFrame(
    wine.data,
    columns=feature_names
)

df["target"] = wine.target


# 3. Explore the dataset
print("First five rows:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nSummary statistics:")
print(df.describe().round(2))


# 4. Check data quality
missing_count = df.isna().sum().sum()
duplicate_count = df.duplicated().sum()

print("\nMissing values:")
print(missing_count)

print("\nDuplicate rows:")
print(duplicate_count)

# The built-in Wine dataset has no missing or duplicate rows,
# so no data cleaning is required for this exercise.


# 5. Analyze grouped statistics by wine class
print("\nAverage values per wine class:")
print(
    df.groupby("target")[
        ["alcohol", "flavanoids", "color_intensity"]
    ]
    .mean()
    .round(2)
)


# 6. Create and save a labelled scatter plot
plt.figure(figsize=(7, 5))

for class_id, class_name in enumerate(class_names):
    subset = df[df["target"] == class_id]

    plt.scatter(
        subset["alcohol"],
        subset["flavanoids"],
        label=class_name
    )

plt.title("Wine: Alcohol vs Flavanoids")
plt.xlabel("Alcohol")
plt.ylabel("Flavanoids")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("wine_scatter.png", dpi=150, bbox_inches="tight")
plt.close()

print("\nScatter plot saved to wine_scatter.png")


# 7. Separate features and target labels, then split the data
X = df[feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 8-9. Build the pipeline, train the model and make predictions
model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# 10. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel accuracy:")
print(round(accuracy, 3))

print("\nConfusion matrix:")
print(
    confusion_matrix(
        y_test,
        y_pred,
        labels=class_labels
    )
)

print("\nClassification report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=class_labels,
        target_names=class_names,
        zero_division=0
    )
)


# 11. Predict the class of one held-out sample
sample = X_test.iloc[[0]]

predicted_class = model.predict(sample)[0]
actual_class = y_test.iloc[0]

predicted_name = class_names[predicted_class]
actual_name = class_names[actual_class]

print("\nExample prediction:")
print("Predicted wine class:", predicted_name)
print("Actual wine class:", actual_name)


# 12. Summarize the capstone results
number_of_features = X.shape[1]
number_of_classes = len(class_names)
number_of_test_samples = len(y_test)

print(
    f"\nConclusion: The model used {number_of_features} numerical "
    f"measurements and Logistic Regression to classify wines into "
    f"{number_of_classes} classes. It achieved {accuracy:.1%} accuracy "
    f"on {number_of_test_samples} unseen wines. The test set is "
    f"relatively small, so performance may vary with a different split."
)
