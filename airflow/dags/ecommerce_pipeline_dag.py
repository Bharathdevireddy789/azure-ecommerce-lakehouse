from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import timedelta

SPARK_CONTAINER = "spark"

default_args = {
    "owner": "srinath",
    "start_date": datetime(2025, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    dag_id="ecommerce_lakehouse_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False
) as dag:

    bronze_task = BashOperator(
        task_id="bronze_ingestion",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && python spark/bronze/ingest_api.py >> logs/bronze.log 2>&1'"
        )
    )

    silver_task = BashOperator(
        task_id="silver_processing",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && python spark/silver/process_silver.py >> logs/silver.log 2>&1'"
        )
    )

    gold_task = BashOperator(
        task_id="gold_processing",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && python spark/gold/process_gold.py >> logs/gold.log 2>&1'"
        )
    )

    warehouse_task = BashOperator(
        task_id="warehouse_loading",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && spark-submit warehouse/load_gold_to_warehouse.py >> logs/warehouse.log 2>&1'"
        )
    )

    bronze_task >> silver_task >> gold_task >> warehouse_task
