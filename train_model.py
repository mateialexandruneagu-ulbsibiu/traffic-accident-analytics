import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

print("===================================")
print("Starting Machine Learning...")
print("===================================")

file_path = r'data\processed\cleaned_accidents.csv'

print("Reading dataset...")

df = pd.read_csv(file_path)

print("Dataset loaded.")
print("Shape:", df.shape)


print("Creating sample...")

df = df.sample(
    n=100000,
    random_state=42
)

print("Sample Shape:", df.shape)


features = [
    'Visibility(mi)',
    'Temperature(F)',
    'Humidity(%)',
    'Wind_Speed(mph)',
    'Hour'
]

target = 'Severity'


df = df.dropna(subset=features + [target])

X = df[features]
y = df[target]

print("Preparing train/test split...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Model trained.")


predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("===================================")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("===================================")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

print("===================================")
print("Training Complete")
print("===================================")

input("Press Enter to exit...")
