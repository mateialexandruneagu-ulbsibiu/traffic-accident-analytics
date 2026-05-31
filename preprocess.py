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
df['Start_Time'] = pd.to_datetime(df['Start_Time'])

df['Hour'] = df['Start_Time'].dt.hour
df['Day'] = df['Start_Time'].dt.day_name()
df['Month'] = df['Start_Time'].dt.month_name()

df['Year'] = df['Start_Time'].dt.year

selected_columns = [
    'Severity',
    'State',
    'City',
    'Weather_Condition',
    'Visibility(mi)',
    'Temperature(F)',
    'Humidity(%)',
    'Wind_Speed(mph)',
    'Hour',
    'Day',
    'Month'
]

cleaned_df = df[selected_columns]

cleaned_df.to_csv('data/processed/cleaned_accidents.csv', index=False)

print("Cleaned dataset saved successfully.")
print("Final Shape:", cleaned_df.shape)
