import json
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = make_classification(
    n_samples=1000,
    n_features=6,
    n_informative=5,
    n_redundant=0,
    random_state=42,
    class_sep=2.0
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

with open("metrics.json", "w") as file:
    json.dump({"accuracy": float(accuracy)}, file, indent=4)

print("Model training completed!")
print("Accuracy:", round(accuracy, 4))
