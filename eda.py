import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

_df = pd.read_csv('data/processed/cleaned_accidents.csv')
_df.head()

plt.figure(figsize=(14,6))
_df['State'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 States by Accident Count')
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(_df['Hour'], bins=24)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Accident Count')
plt.show()

weather_severity = _df.groupby('Weather_Condition')['Severity'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(14,6))
weather_severity.plot(kind='bar')
plt.title('Average Accident Severity by Weather Condition')
plt.ylabel('Average Severity')
plt.show()

numeric_df = _df.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()
