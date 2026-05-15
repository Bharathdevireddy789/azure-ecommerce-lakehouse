import psycopg2
from pyspark.sql import SparkSession

from db_config import DB_CONFIG

spark = (
    SparkSession.builder
    .appName("WarehouseLoader")
    .getOrCreate()
)

category_sales_df = spark.read.parquet(
    "data/processed/gold/category_sales"
)

top_products_df = spark.read.parquet(
    "data/processed/gold/top_products"
)

if category_sales_df.count() == 0:
    raise Exception("Category sales dataset is empty")

conn = psycopg2.connect(**DB_CONFIG)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS category_sales (
    category VARCHAR(255),
    total_sales FLOAT,
    product_count INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS top_products (
    id INT,
    title TEXT,
    category VARCHAR(255),
    price FLOAT,
    rating FLOAT
)
""")

conn.commit()

for row in category_sales_df.collect():

    cursor.execute("""
    INSERT INTO category_sales
    VALUES (%s, %s, %s)
    """, (
        row["category"],
        row["total_sales"],
        row["product_count"]
    ))

for row in top_products_df.collect():

    cursor.execute("""
    INSERT INTO top_products
    VALUES (%s, %s, %s, %s, %s)
    """, (
        row["id"],
        row["title"],
        row["category"],
        row["price"],
        row["rating"]
    ))

conn.commit()

cursor.close()
conn.close()

spark.stop()

print("Warehouse loading completed successfully")