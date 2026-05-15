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
            "bash -lc 'cd /app && python spark/bronze/ingest_api.py'"
        )
    )

    silver_task = BashOperator(
        task_id="silver_processing",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && python spark/silver/process_silver.py'"
        )
    )

    gold_task = BashOperator(
        task_id="gold_processing",
        bash_command=(
            f"docker exec {SPARK_CONTAINER} "
            "bash -lc 'cd /app && python spark/gold/process_gold.py'"
        )
    )

    bronze_task >> silver_task >> gold_task
