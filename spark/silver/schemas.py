from pyspark.sql.types import *

product_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("description", StringType(), True),
    StructField("category", StringType(), True),
    StructField("image", StringType(), True),
    StructField("rating", StructType([
        StructField("rate", DoubleType(), True),
        StructField("count", IntegerType(), True)
    ]), True)
])