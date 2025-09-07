import pytest
from pyspark.sql import SparkSession

@pytest.fixture
def spark():
    spark = SparkSession.builder.master("local[2]").appName("test").getOrCreate()
    yield spark
    spark.stop()
