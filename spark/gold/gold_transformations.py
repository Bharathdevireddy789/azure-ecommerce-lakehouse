from pyspark.sql.functions import *

def category_sales(df):

    return (
        df.groupBy("category")
        .agg(
            round(sum("price"), 2).alias("total_sales"),
            count("id").alias("product_count")
        )
    )


def top_products(df):

    return (
        df.select(
            "id",
            "title",
            "category",
            "price",
            col("rating.rate").alias("rating")
        )
        .orderBy(col("price").desc())
    )