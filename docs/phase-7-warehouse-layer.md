# Phase 7 — Data Warehouse and Analytics Serving Layer

## Overview

Phase 7 introduces the analytics serving layer of the Azure E-Commerce Lakehouse project.

In this phase, Gold-layer analytical datasets are loaded into a PostgreSQL warehouse for downstream analytics, SQL querying, and BI reporting.

This phase transforms the platform from a pure lakehouse pipeline into a hybrid lakehouse + warehouse architecture.

---

# Objectives

The goals of this phase are:

- Load Gold analytics datasets into PostgreSQL
- Create analytics-ready warehouse tables
- Implement structured ETL loading workflows
- Integrate warehouse loading into Airflow orchestration
- Prepare datasets for Power BI reporting

---

# Architecture

```text
Gold Parquet Layer
        ↓
Spark Warehouse Loader
        ↓
PostgreSQL Analytics Warehouse
        ↓
Power BI / SQL Analytics
```

---

# Project Structure

```text
warehouse/
├── load_gold_to_warehouse.py
├── warehouse_queries.sql
├── db_config.py
```

---

# Components

## 1. db_config.py

Contains PostgreSQL connection settings used by the warehouse loader.

### Responsibilities

- Store database connection configuration
- Centralize warehouse connectivity settings

### Example Configuration

```python
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "airflow",
    "user": "airflow",
    "password": "airflow"
}
```

---

## 2. warehouse_queries.sql

Defines warehouse table schemas.

### Warehouse Tables

#### category_sales

Stores aggregated category-level sales metrics.

| Column | Type |
|---|---|
| category | VARCHAR |
| total_sales | FLOAT |
| product_count | INT |

---

#### top_products

Stores top-performing product analytics.

| Column | Type |
|---|---|
| id | INT |
| title | TEXT |
| category | VARCHAR |
| price | FLOAT |
| rating | FLOAT |

---

## 3. load_gold_to_warehouse.py

Main ETL pipeline responsible for loading Gold datasets into PostgreSQL.

### Responsibilities

- Read Gold parquet datasets
- Create warehouse tables
- Validate datasets
- Insert analytical records into PostgreSQL
- Close database connections safely

---

# Warehouse Loading Flow

## Step 1 — Read Gold Layer

The Spark job reads analytical parquet datasets:

```text
data/processed/gold/category_sales
data/processed/gold/top_products
```

---

## Step 2 — Validate Datasets

Basic validation checks ensure datasets are not empty before loading.

Example:

```python
if category_sales_df.count() == 0:
    raise Exception("Category sales dataset is empty")
```

---

## Step 3 — Create Warehouse Tables

Tables are created automatically if they do not already exist.

This allows repeatable local deployments.

---

## Step 4 — Insert Analytical Records

Gold-layer records are inserted into PostgreSQL warehouse tables.

---

# Running the Warehouse Loader

Since Spark is containerized, the warehouse loader is executed using Spark Submit inside the Spark container.

## Command

```bash
docker exec -it spark spark-submit warehouse/load_gold_to_warehouse.py
```

---

# Verifying Warehouse Tables

Connect to PostgreSQL container:

```bash
docker exec -it airflow_postgres psql -U airflow
```

---

## List Tables

```sql
\dt
```

Expected tables:

```text
category_sales
top_products
```

---

## Query Sample Data

```sql
SELECT * FROM category_sales;
```

---

# Airflow Integration

The warehouse loader is integrated into the Airflow DAG pipeline.

## Updated Pipeline Flow

```text
Bronze Ingestion
        ↓
Silver Processing
        ↓
Gold Processing
        ↓
Warehouse Loading
```

---

## Airflow Warehouse Task

```python
warehouse_task = BashOperator(
    task_id="warehouse_loading",
    bash_command="cd /app && spark-submit warehouse/load_gold_to_warehouse.py"
)
```

---

# Design Decisions

## Why PostgreSQL Instead of Snowflake Initially?

PostgreSQL was chosen for the initial warehouse layer because:

- Faster local development
- Easier debugging
- Existing Docker infrastructure
- Simpler onboarding
- Strong SQL support

The architecture is designed so Snowflake migration can be added later with minimal changes.

---

## Why Use Parquet as Intermediate Storage?

Parquet provides:

- Columnar storage
- Compression
- Faster Spark reads
- Analytics optimization
- Industry-standard data lake format

---

## Why Separate Gold and Warehouse Layers?

The Gold layer stores analytical datasets in the lakehouse.

The Warehouse layer serves:

- BI dashboards
- SQL analytics
- Reporting tools
- Business consumption

This separation improves scalability and architecture clarity.

---

# Technologies Used

| Component | Technology |
|---|---|
| Processing Engine | Apache Spark |
| Warehouse | PostgreSQL |
| Orchestration | Apache Airflow |
| Storage Format | Parquet |
| Containerization | Docker |

---

# Key Learnings

This phase demonstrates:

- Warehouse engineering
- ETL loading workflows
- Analytics serving architecture
- Spark-to-SQL integration
- Airflow orchestration integration
- Structured analytical modeling

---

# Current Pipeline Architecture

```text
FakeStore API
      ↓
Kafka
      ↓
Bronze Layer
      ↓
Silver Layer
      ↓
Gold Layer
      ↓
PostgreSQL Warehouse
      ↓
Analytics / BI
```

---

# Next Phase

Phase 8 will introduce:

- Power BI dashboards
- KPI visualizations
- Revenue analytics
- Business reporting
- Executive dashboarding