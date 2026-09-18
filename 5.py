import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = {
    "length": [20, 25, 30, 80, 90, 100, 22, 28, 85, 95],
    "https": [1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    "special_chars": [0, 0, 1, 4, 5, 6, 0, 1, 5, 4],
    "label": [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["length", "https", "special_chars"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = SVC(kernel="linear")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("SVM URL Classification")
print("----------------------")
print("Accuracy:", accuracy * 100, "%")

new_url = [[70, 0, 4]]
prediction = model.predict(new_url)

if prediction[0] == 1:
    print("New URL: Malicious")
else:
    print("New URL: Legitimate")