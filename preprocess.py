import pandas as pd
import numpy as np

file_path = 'data/raw/US_Accidents_March23.csv'
df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

df.drop_duplicates(inplace=True)

important_columns = [
    'Severity',
    'Weather_Condition',
    'Visibility(mi)',
    'Temperature(F)'
]

for col in important_columns:
    df[col].fillna(df[col].median() if df[col].dtype != 'O' else 'Unknown', inplace=True)
