# Final capstone: Data Analysis and AI Pipeline
# Goal: Independently build a complete data-analysis and machine-learning project, using the built-in Wine dataset so that you're applying the skills to data different from the Iris dataset.
# 1. Load the Wine dataset using scikit-learn
# 2. Create a pandas DataFrame containing the features and class label.
# 3. Inspect the first rows, dataset dimensions and summary statistics.
# 4. Check for missing values and duplicate rows.
# 5. Calculate useful grouped statistics by class.
# 6. Create and save a labelled scatter plot using two numerical features.
# 7. Split features and labels into training and testing sets using stratification.
# 8. Build a Pipeline containing StandardScaler and a classifier.
# 9. Train the model and predict the test labels.
# 10. Report accuracy, confusion matrix and classification report.
# 11. Predict the class of at least one held-out sample.
# 12. Write a short conclusion explaining what the model did and how well it performed.


# useful hint: the Wine dataset's class labels are available through wine.target, and their names are in wine.target_names. Use the feature names supplied by wine.feature_names rather than manually typing out every column name.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 1-2. Load the dataset and build a DataFrame (features + class label)
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target


# 3. Inspect
print(df.head())
print("\nShape (rows, columns):", df.shape)
print(df.describe().round(2))


# 4. Quality checks
print("\nMissing values:", df.isna().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
# Both are 0, so no cleaning is needed.


# 5. Grouped statistics by class
print("\nAverage values per class:")
print(df.groupby("target")[["alcohol", "flavanoids", "color_intensity"]].mean().round(2))


# 6. Labelled scatter plot of two features, coloured by class
plt.figure(figsize=(7, 5))
for class_id, name in enumerate(wine.target_names):
    subset = df[df["target"] == class_id]
    plt.scatter(subset["alcohol"], subset["flavanoids"], label=name)
plt.title("Wine: Alcohol vs Flavanoids")
plt.xlabel("Alcohol")
plt.ylabel("Flavanoids")
plt.legend()
plt.grid(True)
plt.savefig("wine_scatter.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nScatter plot saved to wine_scatter.png")


# 7. Split with stratification
X = df[wine.feature_names]
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# 8-9. Pipeline: scale features, then Logistic Regression; train and predict
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# 10. Evaluate
print("\nAccuracy:", round(accuracy_score(y_test, y_pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=wine.target_names))


# 11. Predict one held-out sample
sample = X_test.iloc[[0]]                  # double brackets keep it a table
predicted = wine.target_names[model.predict(sample)[0]]
actual = wine.target_names[y_test.iloc[0]]
print(f"Sample prediction: {predicted} | Actual: {actual}")


# 12. Conclusion
accuracy = accuracy_score(y_test, y_pred)
print(f"\nConclusion: The model scaled 13 chemical measurements and used "
      f"Logistic Regression to classify wines into 3 classes. It scored "
      f"{accuracy:.1%} on 36 unseen wines. The test set is small, so "
      f"results could vary with a different split.")
