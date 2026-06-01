import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("===================================")
print("Starting EDA...")
print("===================================")

input_file = r'C:\Users\admin\Desktop\Neagu Matei Big Data Project\traffic-accident-analytics\data\processed\cleaned_accidents.csv'

screenshots_folder = r'C:\Users\admin\Desktop\Neagu Matei Big Data Project\traffic-accident-analytics\screenshots'

print("Checking dataset location...")

if not os.path.exists(input_file):
    print("ERROR: Dataset not found.")
    print(input_file)
    input("Press Enter to exit...")
    quit()

print("Dataset found.")

print("Creating screenshots folder...")

os.makedirs(
    screenshots_folder,
    exist_ok=True
)

print("Reading data...")

df = pd.read_csv(input_file)

print("Dataset loaded successfully.")
print("Dataset Shape:", df.shape)

print("Creating sample dataset...")

sample_df = df.sample(
    n=100000,
    random_state=42
)

print("Sample Shape:", sample_df.shape)

sns.set_style("whitegrid")

# ==================================================
# Top States
# ==================================================

print("Generating Top States chart...")

plt.figure(figsize=(12, 6))

sample_df["State"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 States by Accident Count")
plt.xlabel("State")
plt.ylabel("Number of Accidents")

plt.tight_layout()

plt.savefig(
    os.path.join(
        screenshots_folder,
        "top_states.png"
    )
)

plt.close()

print("Saved: top_states.png")

# ==================================================
# Accidents by Hour
# ==================================================

print("Generating Hour Distribution chart...")

plt.figure(figsize=(12, 6))

sample_df["Hour"].hist(bins=24)

plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Accident Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        screenshots_folder,
        "accidents_by_hour.png"
    )
)

plt.close()

print("Saved: accidents_by_hour.png")

# ==================================================
# Severity Distribution
# ==================================================

print("Generating Severity chart...")

plt.figure(figsize=(10, 6))

sample_df["Severity"] \
    .value_counts() \
    .sort_index() \
    .plot(kind="bar")

plt.title("Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        screenshots_folder,
        "severity_distribution.png"
    )
)

plt.close()

print("Saved: severity_distribution.png")

# ==================================================
# Weather vs Severity
# ==================================================

print("Generating Weather Severity chart...")

weather_severity = (
    sample_df
    .groupby("Weather_Condition")["Severity"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(14, 6))

weather_severity.plot(kind="bar")

plt.title("Average Severity by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Average Severity")

plt.tight_layout()

plt.savefig(
    os.path.join(
        screenshots_folder,
        "weather_severity.png"
    )
)

plt.close()

print("Saved: weather_severity.png")

# ==================================================
# Correlation Heatmap
# ==================================================

print("Generating Correlation Heatmap...")

numeric_df = sample_df.select_dtypes(
    include=["float64", "int64"]
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    os.path.join(
        screenshots_folder,
        "correlation_heatmap.png"
    )
)

plt.close()

print("Saved: correlation_heatmap.png")

print("===================================")
print("EDA completed successfully.")
print("Charts saved to:")
print(screenshots_folder)
print("===================================")

input("Press Enter to exit...")
