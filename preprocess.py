import os
import pandas as pd

input_file = r'C:\Users\admin\Desktop\Neagu Matei Big Data Project\traffic-accident-analytics\data\raw\US_Accidents_March23.csv'
output_file = r'C:\Users\admin\Desktop\Neagu Matei Big Data Project\traffic-accident-analytics\data\processed\cleaned_accidents.csv'

print("Loading dataset...")

df = pd.read_csv(input_file)

print("Dataset loaded successfully.")
print("Original Shape:", df.shape)

df = df.drop_duplicates()

print("Duplicates removed.")
print("Current Shape:", df.shape)

columns_to_clean = [
    'Severity',
    'Weather_Condition',
    'Visibility(mi)',
    'Temperature(F)'
]

for col in columns_to_clean:
    if col in df.columns:

        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna('Unknown')

print("Missing values handled.")

df['Start_Time'] = pd.to_datetime(
    df['Start_Time'],
    format='mixed',
    errors='coerce'
)
print("Missing dates:", df['Start_Time'].isna().sum())

df['Hour'] = df['Start_Time'].dt.hour
df['Day'] = df['Start_Time'].dt.day_name()
df['Month'] = df['Start_Time'].dt.month_name()
df['Year'] = df['Start_Time'].dt.year

print("Date features created.")

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

selected_columns = [col for col in selected_columns if col in df.columns]

cleaned_df = df[selected_columns]

os.makedirs(os.path.dirname(output_file), exist_ok=True)

cleaned_df.to_csv(output_file, index=False)

print("===================================")
print("Cleaned dataset saved successfully.")
print("Output:", output_file)
print("Final Shape:", cleaned_df.shape)
print("===================================")

input("Press Enter to exit...")
