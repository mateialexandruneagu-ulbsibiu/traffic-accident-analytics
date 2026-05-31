from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

spark = SparkSession.builder \
    .appName("Traffic Accident Analysis") \
    .getOrCreate()

spark_df = spark.read.csv(
    'data/processed/cleaned_accidents.csv',
    header=True,
    inferSchema=True
)

spark_df.printSchema()

state_accidents = spark_df.groupBy('State') \
    .agg(count('*').alias('Accident_Count')) \
    .orderBy('Accident_Count', ascending=False)

state_accidents.show(10)

weather_analysis = spark_df.groupBy('Weather_Condition') \
    .agg(avg('Severity').alias('Average_Severity')) \
    .orderBy('Average_Severity', ascending=False)

weather_analysis.show(10)

spark.stop()
