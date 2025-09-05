#from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col
from sparkml.utils.spark_session import get_spark_session
import sys

def run_wordcount(input_path, output_path):
    spark = get_spark_session()
    result = wordcount(spark, input_path)
    result.show(100,False)
    result.coalesce(1).write.mode("overwrite").parquet(output_path)
    spark.stop()

def wordcount(spark, input_path):
    df = spark.read.text(input_path)
    words_df = df.select(explode(split(col("value"), " ")).alias("word"))
    result =  words_df.groupBy("word").count().orderBy(col("count").desc())#orderBy(["count"], ascending=[False])
    return result

# permet de lancer le job directement
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wordcount.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    run_wordcount(input_path, output_path)

