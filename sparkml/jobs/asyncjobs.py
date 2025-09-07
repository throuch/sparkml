import sys, asyncio
from sparkml.utils.spark_session import get_spark_session

def count_even(df):
    return df.filter("id % 2 = 0").count()

def count_odd(df):
    return df.filter("id % 2 = 1").count()

async def twoqueries(df):
    r1, r2 = await asyncio.gather(
        asyncio.to_thread(lambda : count_even(df)),
        asyncio.to_thread(lambda : count_odd(df)),
        return_exceptions=True
    )
    print(f"Even count: {r1}, Odd count: {r2}")

def run_twoqueries():
    spark = get_spark_session("2 queries")
    df = spark.range(1, 1000000)
    asyncio.run(twoqueries(df))
    spark.stop()

if __name__ == "__main__":
    run_twoqueries()
