from pyspark.sql import SparkSession

from gold_transformations import (
    category_sales,
    top_products
)

SILVER_PATH = "data/processed/silver/products"
GOLD_PATH = "data/processed/gold"

spark = (
    SparkSession.builder
    .appName("GoldLayerProcessing")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet(SILVER_PATH)

if df.count() == 0:
    raise Exception("Silver layer dataset is empty")

category_sales_df = category_sales(df)

top_products_df = top_products(df)

category_sales_df.show()

top_products_df.show(5)

(
    category_sales_df.write
    .mode("overwrite")
    .parquet(f"{GOLD_PATH}/category_sales")
)

(
    top_products_df.write
    .mode("overwrite")
    .parquet(f"{GOLD_PATH}/top_products")
)

print("Gold layer processing completed successfully")

spark.stop()
