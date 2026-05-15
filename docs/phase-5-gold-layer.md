# Phase 5 — Gold Layer Analytics

## Objective

The purpose of the Gold layer is to transform cleaned Silver-layer datasets into business-ready analytical datasets optimized for reporting and dashboard consumption.

This phase introduces:
- Business aggregations
- KPI generation
- Analytical datasets
- Gold-layer parquet outputs
- Spark-based analytical processing

---

# Architecture Flow

```text
Bronze Layer (Raw JSON)
        ↓
Silver Layer (Clean Structured Data)
        ↓
Gold Layer (Business Analytics)
```

The Gold layer represents curated datasets intended for:
- Business Intelligence
- Reporting dashboards
- Analytics consumption
- Executive KPIs

---

# Project Structure

```text
spark/
├── gold/
│   ├── process_gold.py
│   ├── gold_transformations.py
```

---

# Gold Layer Datasets

The following datasets are generated:

| Dataset | Description |
|---|---|
| category_sales | Revenue aggregated by category |
| top_products | Highest-priced products with ratings |

---

# Gold Transformations

## File

```text
spark/gold/gold_transformations.py
```

This module contains reusable analytical transformations.

---

## category_sales()

Aggregates:
- total revenue by category
- product counts by category

### Logic

```python
groupBy("category")
sum("price")
count("id")
```

### Output Columns

| Column | Description |
|---|---|
| category | Product category |
| total_sales | Total revenue |
| product_count | Number of products |

---

## top_products()

Creates an analytical dataset of top-priced products.

### Output Columns

| Column | Description |
|---|---|
| id | Product ID |
| title | Product title |
| category | Product category |
| price | Product price |
| rating | Product rating |

### Sorting Logic

Products are sorted in descending order by:
- price

---

# Main Gold Processing Pipeline

## File

```text
spark/gold/process_gold.py
```

This script:
1. Reads Silver parquet datasets
2. Applies Gold transformations
3. Writes Gold parquet outputs

---

# Input Paths

```python
SILVER_PATH = "data/processed/silver/products"
```

---

# Output Paths

```python
data/processed/gold/category_sales
data/processed/gold/top_products
```

---

# Spark Execution Workflow

The project uses a containerized Spark environment.

Spark jobs are executed using:
- spark-submit
- Docker container execution

---

# Running the Gold Pipeline

## Start Containers

```bash
docker compose up -d
```

---

## Execute Gold Layer

```bash
docker exec -it spark spark-submit spark/gold/process_gold.py
```

---

# Data Validation

Basic validation checks were implemented.

## Empty Dataset Validation

```python
if df.count() == 0:
    raise Exception("Silver layer dataset is empty")
```

This prevents downstream Gold processing on invalid datasets.

---

# Output Format

The Gold layer stores datasets in:
- Parquet format

### Why Parquet?

Parquet provides:
- columnar storage
- compression
- faster analytical queries
- Spark optimization

---

# Sample Output Structure

```text
data/
├── processed/
│   ├── gold/
│   │   ├── category_sales/
│   │   ├── top_products/
```

---

# Logging and Debugging

The Gold pipeline prints:
- aggregation outputs
- top product samples
- pipeline completion messages

Example:

```python
category_sales_df.show()
top_products_df.show(5)
```

---

# Key Engineering Concepts Demonstrated

This phase demonstrates:

- Medallion architecture
- Analytical data modeling
- PySpark transformations
- Aggregations and KPIs
- Containerized Spark execution
- Modular pipeline design
- Data validation
- Parquet optimization

---

# Git Commit History

Example commits for this phase:

```bash
git commit -m "Add Gold layer analytical transformations"

git commit -m "Implement category sales aggregation pipeline"

git commit -m "Add top products analytics dataset"

git commit -m "Configure containerized Spark execution workflow"
```

---

# Final Outcome

At the end of Phase 5, the project now supports:

- Bronze raw ingestion
- Silver cleaned datasets
- Gold analytical datasets
- Spark-based transformations
- Containerized execution
- Business-ready outputs

The project architecture now resembles a modern lakehouse analytics platform.