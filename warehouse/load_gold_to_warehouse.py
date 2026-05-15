import psycopg2
from psycopg2.extras import execute_values
from pyspark.sql import SparkSession

from db_config import DB_CONFIG

spark = (
    SparkSession.builder
    .appName("WarehouseLoader")
    .master("local[*]")
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

if top_products_df.count() == 0:
    raise Exception("Top products dataset is empty")

conn = psycopg2.connect(**DB_CONFIG)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS category_sales (
    category VARCHAR(255) PRIMARY KEY,
    total_sales FLOAT,
    product_count INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS top_products (
    id INT PRIMARY KEY,
    title TEXT,
    category VARCHAR(255),
    price FLOAT,
    rating FLOAT
)
""")

conn.commit()

# Gold tables are full snapshots, so reload them atomically on each Airflow run.
cursor.execute("TRUNCATE TABLE category_sales, top_products")

cursor.execute("""
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conrelid = 'category_sales'::regclass
        AND contype = 'p'
    ) THEN
        ALTER TABLE category_sales
        ADD CONSTRAINT category_sales_pkey PRIMARY KEY (category);
    END IF;

    IF NOT EXISTS (
        SELECT 1
        FROM pg_constraint
        WHERE conrelid = 'top_products'::regclass
        AND contype = 'p'
    ) THEN
        ALTER TABLE top_products
        ADD CONSTRAINT top_products_pkey PRIMARY KEY (id);
    END IF;
END $$;
""")

category_sales_rows = [
    (
        row["category"],
        row["total_sales"],
        row["product_count"]
    )
    for row in category_sales_df.collect()
]

top_products_rows = [
    (
        row["id"],
        row["title"],
        row["category"],
        row["price"],
        row["rating"]
    )
    for row in top_products_df.collect()
]

execute_values(
    cursor,
    """
    INSERT INTO category_sales (category, total_sales, product_count)
    VALUES %s
    """,
    category_sales_rows
)

execute_values(
    cursor,
    """
    INSERT INTO top_products (id, title, category, price, rating)
    VALUES %s
    """,
    top_products_rows
)

conn.commit()

cursor.close()
conn.close()

spark.stop()

print("Warehouse loading completed successfully")
