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
