from pyspark.sql import SparkSession

def create_df():
    spark = SparkSession.builder \
        .appName("MonProjetPySpark") \
        .master("local[*]") \
        .getOrCreate()

    data = [(1, "Alice"), (2, "Bob")]
    df = spark.createDataFrame(data, ["id", "name"])


    return df

def main():
    create_df()



if __name__ == "__main__":
    main()
