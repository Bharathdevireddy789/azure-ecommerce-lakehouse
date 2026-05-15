# Phase 6 — Airflow Orchestration

## Overview

In this phase, Apache Airflow was integrated into the Azure E-Commerce Lakehouse project to orchestrate the end-to-end data pipeline.

The orchestration layer automates the execution flow between:

1. Bronze Layer ingestion
2. Silver Layer transformations
3. Gold Layer analytics generation

This phase transforms the project from isolated ETL scripts into a production-style orchestrated data platform.

---

# Objectives

The goals of this phase were:

- Introduce workflow orchestration
- Automate pipeline execution
- Establish task dependencies
- Implement retry handling
- Enable centralized monitoring
- Simulate production scheduling workflows

---

# Architecture

## Pipeline Flow

```text
Bronze Ingestion
        ↓
Silver Processing
        ↓
Gold Processing
```

Airflow manages task execution order and ensures downstream tasks execute only after upstream tasks complete successfully.

---

# Technologies Used

| Component | Technology |
|---|---|
| Orchestration | Apache Airflow |
| Executor | LocalExecutor |
| Metadata Database | PostgreSQL |
| Processing Engine | Apache Spark |
| Containerization | Docker |

---

# Docker Configuration

The Airflow service was added to the Docker Compose infrastructure.

---

# DAG Implementation

## DAG File

```text
airflow/dags/ecommerce_pipeline_dag.py
```

---

# DAG Responsibilities

The DAG orchestrates:

| Task | Description |
|---|---|
| bronze_ingestion | Fetch raw product data from API |
| silver_processing | Execute Spark Silver transformations |
| gold_processing | Generate Gold analytics datasets |

---

# DAG Structure

```python
bronze_task >> silver_task >> gold_task
```

This dependency chain ensures:

1. Raw data ingestion completes first
2. Cleaned Silver datasets are generated second
3. Gold analytics datasets are created last

---

# Key Features Implemented

## Task Dependencies

The pipeline enforces strict execution order between Bronze, Silver, and Gold layers.

---

## Retry Handling

Airflow retries failed tasks automatically.

Configuration:

```python
"retries": 2,
"retry_delay": timedelta(minutes=1)
```

This improves fault tolerance and pipeline reliability.

---

## Scheduling

The DAG is configured to run daily.

```python
schedule="@daily"
```

---

## Monitoring

Airflow UI provides:

- DAG monitoring
- Task execution tracking
- Failure visibility
- Log inspection

---

# Running the Pipeline

## Start Containers

```bash
docker compose up -d
```

---

## Open Airflow UI

```text
http://localhost:8080
```

### Credentials

```text
username: admin
password: admin
```

---

# Triggering the Pipeline

1. Open Airflow UI
2. Enable DAG
3. Click "Trigger DAG"

---

# Spark Execution Inside Containers

Spark jobs are executed inside the dedicated Spark container using:

```bash
spark-submit
```

This simulates real-world distributed Spark execution workflows.

---

# Benefits of This Architecture

This orchestration design provides:

- Modular pipeline architecture
- Scalable workflow execution
- Centralized scheduling
- Improved maintainability
- Production-style execution patterns

---

# Screenshots

Recommended screenshots for documentation:

- Airflow DAG graph view
- Successful DAG execution
- Task logs
- Spark job execution
- Gold layer outputs

Store screenshots inside:

```text
docs/screenshots/
```

---

# Learning Outcomes

This phase demonstrates practical experience with:

- Apache Airflow
- DAG orchestration
- Workflow automation
- Spark job scheduling
- Dockerized infrastructure
- Fault-tolerant pipelines
- Production ETL design

---

# Current Pipeline Architecture

```text
FakeStore API
        ↓
Kafka Streaming
        ↓
Bronze Layer (Raw JSON)
        ↓
Silver Layer (Cleaned Parquet)
        ↓
Gold Layer (Analytics Tables)
        ↓
Airflow Orchestration
```

---

# Next Phase

The next phase introduces the analytics serving layer using:

- Snowflake or PostgreSQL
- Fact and dimension modeling
- Warehouse-style analytics tables
- BI integrations