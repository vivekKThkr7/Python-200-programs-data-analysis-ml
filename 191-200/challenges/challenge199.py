# Train and evaluate a model ; Train a different classifier and evaluate its performance.
# using the iris dataset, build a machine-learning workflow that:
# 1. Splits the data into training and test sets.
# 2. uses StandardScaler followed by KNeighborsClassifier(n_neighbors=5) in a pipeline.
# 3. Trains using .fit().
# 4. Predicts using .predict()
# 5. Reports accuracy, confusion matrix and classification report.
# 6. Compare the accuracy with your Logistic Regression model from Program 199.

# Hint:
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)


# KNN : classifies by looking at the 5 nearest training  samples.
knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))

knn.fit(X_train, y_train)  # learn from training data
knn_pred = knn.predict(X_test)  # predict unseen data
knn_acc = accuracy_score(y_test, knn_pred)

print("KNN accuracy:", round(knn_acc, 3))
print("Confusion matrix:\n", confusion_matrix(y_test, knn_pred))
print(classification_report(y_test, knn_pred, target_names=iris.target_names))


# Logistic Regression on the SAME split, for comparison
logreg = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
logreg.fit(X_train, y_train)
log_acc = accuracy_score(y_test, logreg.predict(X_test))

print(f"Logistic Regression accuracy: {log_acc:.3f}")
print(f"KNN accuracy:                 {knn_acc:.3f}")
print("Note: with only 30 test samples, one sample changes accuracy by "
      "about 3%, so a small gap does not prove one model is better.")
