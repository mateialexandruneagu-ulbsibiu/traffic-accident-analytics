import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('data/processed/cleaned_accidents.csv')

encoder = LabelEncoder()

categorical_columns = [
    'State',
    'City',
    'Weather_Condition',
    'Day',
    'Month'
]

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col].astype(str))

X = df[[
    'State',
    'City',
    'Weather_Condition',
    'Visibility(mi)',
    'Temperature(F)',
    'Humidity(%)',
    'Wind_Speed(mph)',
    'Hour'
]]

y = df['Severity']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print(classification_report(y_test, predictions))
