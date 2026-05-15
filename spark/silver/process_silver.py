from pyspark.sql import SparkSession
from pathlib import Path

from schemas import product_schema
from transformations import clean_products, validate_products

# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Bronze directory
BRONZE_DIR = BASE_DIR / "data/raw/products"

# Silver output
SILVER_PATH = str(BASE_DIR / "data/processed/silver/products")

# Collect all JSON files
json_files = [str(file) for file in BRONZE_DIR.glob("*.json")]

if not json_files:
    raise Exception(f"No JSON files found in {BRONZE_DIR}")

print("JSON files found:")
for file in json_files:
    print(file)

spark = (
    SparkSession.builder
    .appName("SilverLayerProcessing")
    .getOrCreate()
)

# Read files
df = (
    spark.read
    .schema(product_schema)
    .json(json_files)
)

# Transformations
cleaned_df = clean_products(df)

validated_df = validate_products(cleaned_df)

# Write Silver layer
(
    validated_df.write
    .mode("overwrite")
    .parquet(SILVER_PATH)
)

print(f"\nSilver data written to:\n{SILVER_PATH}")

spark.stop()