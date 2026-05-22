from pyspark.sql.functions import col, count, round, sum as spark_sum


def category_sales(df):

    return (
        df.groupBy("category")
        .agg(
            round(spark_sum("price"), 2).alias("total_sales"),
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
