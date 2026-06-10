from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg

print("===================================")
print("Starting PySpark Analysis...")
print("===================================")

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Traffic Analytics") \
    .getOrCreate()

print("Spark Session Created.")

file_path = r'data\processed\cleaned_accidents.csv'

print("Loading dataset...")

df = spark.read.option("header", True).csv(file_path)

print("Dataset Loaded.")

print("Rows:", df.count())
print("Columns:", len(df.columns))

print("===================================")
print("Top States by Accident Count")
print("===================================")

df.groupBy("State") \
    .agg(count("*").alias("Accident_Count")) \
    .orderBy("Accident_Count", ascending=False) \
    .show(10)

print("===================================")
print("Average Severity by Weather")
print("===================================")

df.groupBy("Weather_Condition") \
    .agg(avg("Severity").alias("Average_Severity")) \
    .orderBy("Average_Severity", ascending=False) \
    .show(10)

print("===================================")
print("PySpark Analysis Complete")
print("===================================")

input("Press Enter to exit...")

spark.stop()
