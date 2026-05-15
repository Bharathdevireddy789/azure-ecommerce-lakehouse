# Phase 4 — Silver Layer Processing

## Overview

This phase implements the Silver layer of the medallion architecture for the Azure E-Commerce Lakehouse project.

The Silver layer transforms raw Bronze layer JSON data into clean, validated, analytics-ready parquet datasets using PySpark.

This phase introduces:
- PySpark ETL processing
- schema enforcement
- data cleaning
- validation checks
- parquet optimization
- modular transformation design

---

# Architecture Flow

```text
FakeStore API
      ↓
Bronze Layer (Raw JSON)
      ↓
PySpark Processing
      ↓
Data Cleaning & Validation
      ↓
Silver Layer (Parquet)
```

---

# Objectives

The goal of this phase is to:

- Read raw Bronze layer JSON files
- Enforce explicit schemas
- Clean inconsistent data
- Remove duplicates
- Standardize fields
- Add processing metadata
- Store optimized parquet files

---

# Project Structure

```text
azure-ecommerce-lakehouse/

├── spark/
│   ├── bronze/
│   │   ├── ingest_api.py
│   │   ├── kafka_producer.py
│   │   ├── save_raw_data.py
│   │   └── utils.py
│   │
│   ├── silver/
│   │   ├── process_silver.py
│   │   ├── schemas.py
│   │   └── transformations.py
│
├── data/
│   ├── raw/
│   │   └── products/
│   │
│   └── processed/
│       └── silver/
│           └── products/
```

---

# Technologies Used

| Component | Technology |
|---|---|
| Data Processing | PySpark |
| Streaming | Kafka |
| Containerization | Docker |
| Message Broker | Apache Kafka |
| Storage Format | Parquet |
| Data Source | FakeStore API |
| Language | Python |

---

# Docker Infrastructure

Docker Compose is used to provision local infrastructure services.

## Services

### PostgreSQL
Used for future Airflow metadata storage.

### Zookeeper
Required dependency for Kafka.

### Kafka
Used for streaming product events.

---

# Docker Setup

## Start Containers

```bash
docker compose up -d
```

## Verify Running Containers

```bash
docker ps
```

Expected containers:
- airflow_postgres
- zookeeper
- kafka

---

# Kafka Topic Setup

## Access Kafka Container

```bash
docker exec -it kafka bash
```

## Create Kafka Topic

```bash
kafka-topics --create \
--topic orders \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

## Verify Topic

```bash
kafka-topics --list --bootstrap-server localhost:9092
```

---

# Bronze Layer Summary

The Bronze layer performs raw ingestion of e-commerce product data.

## Features

- FakeStore API ingestion
- Kafka producer pipeline
- Raw JSON archival
- Timestamped file storage
- Logging support

## Raw Data Storage

```text
data/raw/products/
```

Example output:

```text
products_20260515_120001.json
```

---

# Silver Layer Processing

The Silver layer reads raw Bronze data and performs structured transformations.

---

# Schema Enforcement

Explicit schemas are defined using PySpark StructType.

File:

```text
spark/silver/schemas.py
```

Benefits:
- Prevents schema drift
- Improves Spark performance
- Ensures consistent datatypes

---

# Transformations

File:

```text
spark/silver/transformations.py
```

## Transformations Applied

### Deduplication

```python
dropDuplicates(["id"])
```

Removes duplicate product records.

---

### Standardization

```python
lower(col("category"))
```

Converts category names to lowercase.

---

### String Cleanup

```python
trim(col("title"))
```

Removes unnecessary whitespace.

---

### Processing Timestamp

```python
current_timestamp()
```

Adds ETL processing metadata.

---

# Data Validation

Validation checks are implemented before writing Silver output.

Example validation:
- Remove records with null prices

```python
filter(col("price").isNotNull())
```

---

# Silver Layer Output

Processed datasets are stored as parquet files.

Output path:

```text
data/processed/silver/products/
```

---

# Why Parquet?

Parquet is used because it provides:

- Columnar storage
- Better compression
- Faster analytics queries
- Spark optimization
- Reduced storage cost

---

# Running the Silver Pipeline

## Execute Processing Script

```bash
python spark/silver/process_silver.py
```

Expected output:

```text
Silver layer processing completed successfully
```

---

# Logging

Basic logging support is implemented for monitoring pipeline execution.

File:

```text
spark/bronze/utils.py
```

Logging format:

```text
timestamp - log level - message
```

---

# Engineering Design Decisions

## Why Separate Bronze and Silver Layers?

This follows medallion architecture principles:
- Bronze stores immutable raw data
- Silver stores cleaned validated data

This improves:
- traceability
- reprocessing capability
- debugging
- scalability

---

## Why Modularize Transformations?

Separating:
- schemas
- transformations
- processing logic

improves:
- maintainability
- readability
- scalability

---

# Key Learnings

This phase demonstrates:

- PySpark ETL development
- Data lake architecture
- Kafka integration
- Schema enforcement
- Data validation
- Parquet optimization
- Modular pipeline design
- Docker-based local infrastructure

---

# Future Enhancements

Upcoming phases will introduce:

- Gold layer aggregations
- Airflow orchestration
- Snowflake warehouse loading
- Power BI dashboards
- CI/CD pipelines
- Terraform infrastructure
- Azure cloud deployment

---

# Current Status

Completed:
- Bronze ingestion layer
- Kafka producer
- Docker infrastructure
- Silver layer ETL pipeline

Next:
- Gold analytics layer