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
