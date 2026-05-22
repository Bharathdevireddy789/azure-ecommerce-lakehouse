from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("SilverTest")
    .getOrCreate()
)


def test_spark_session():

    assert spark is not None
