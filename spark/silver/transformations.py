from pyspark.sql.functions import *

def clean_products(df):

    cleaned_df = (
        df
        .dropDuplicates(["id"])
        .withColumn("title", trim(col("title")))
        .withColumn("category", lower(col("category")))
        .withColumn("processed_timestamp", current_timestamp())
    )

    return cleaned_df


def validate_products(df):

    validated_df = df.filter(col("price").isNotNull())

    return validated_df