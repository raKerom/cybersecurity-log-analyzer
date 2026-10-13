
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned dataset
df = pd.read_csv("processed_logs.csv")

# Separate features and target
X = df[["event_type", "failed_attempts", "severity"]]
y = df["label"]

# Convert categorical features into numeric columns
X = pd.get_dummies(
    X,
    columns=["event_type", "severity"],
    dtype=int
)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Feature preparation completed!")
print("Training rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])
print("Number of features:", X_train.shape[1])

print("\nTraining label counts:")
print(y_train.value_counts())

print("\nTesting label counts:")
print(y_test.value_counts())




###  Training Model



from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Create and train the model
model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Make predictions on unseen test data
y_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Evaluation")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save the trained model
import joblib

joblib.dump(model, "security_model.pkl")
print("\nModel saved as security_model.pkl")
