from pyspark.sql import SparkSession

def get_spark_session(app_name="sparkml"):
    return SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
