# Azure E-Commerce Lakehouse

## Overview

This project demonstrates an end-to-end modern data engineering platform using Azure cloud technologies and open-source tools.

The platform ingests both batch and streaming e-commerce data, processes it through a Medallion Architecture (Bronze/Silver/Gold), and serves analytics-ready data through a warehouse and dashboard layer.

The project is designed to simulate a production-grade cloud data engineering system.

---

# Architecture

Architecture diagram will be added during later phases.

Planned architecture:

FakeStore API / Kafka Streams
            ↓
Azure Data Lake Gen2 (Bronze)
            ↓
Databricks + PySpark
            ↓
Silver Layer
            ↓
Gold Layer
            ↓
Snowflake Warehouse
            ↓
Power BI Dashboard

---

# Tech Stack

| Layer | Technology |
|---|---|
| Cloud | Azure |
| Storage | Azure Data Lake Gen2 |
| Processing | PySpark |
| Streaming | Kafka |
| Orchestration | Apache Airflow |
| Warehouse | Snowflake |
| Transformation | dbt |
| Infrastructure | Terraform |
| Containerization | Docker |
| Visualization | Power BI |
| Language | Python |

---

# Project Goals

- Build scalable batch and streaming pipelines
- Implement Medallion Architecture
- Create production-style orchestration workflows
- Demonstrate CI/CD practices
- Simulate enterprise-grade cloud data engineering
- Showcase Azure Data Engineering skills for employers

---

# Repository Structure

```text
azure-ecommerce-lakehouse/
│
├── README.md
├── .gitignore
├── requirements.txt
├── docker-compose.yml
│
├── architecture/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── airflow/
│   ├── dags/
│
├── spark/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│
├── kafka/
│
├── snowflake/
│
├── dashboards/
│
├── terraform/
│
├── tests/
│
└── docs/
```

---

# Current Progress

| Phase | Status |
|---|---|
| Phase 1 — Project Initialization | Complete |
| Phase 2 — Local Development Environment | Complete |
| Phase 3 — Bronze Layer Ingestion | Complete |
| Phase 4 — Spark Transformations | Complete |
| Phase 5 — Silver Layer | In Progress |
| Phase 6 — Gold Layer | Planned |
| Phase 7 — Airflow Orchestration | Planned |
| Phase 8 — Snowflake Warehouse | Planned |
| Phase 9 — Power BI Dashboards | Planned |
| Phase 10 — CI/CD | Planned |
| Phase 11 — Terraform Infrastructure | Planned |

---

## Silver Layer

The Silver layer performs structured ETL transformations using PySpark.

Features:
- Schema enforcement
- Deduplication
- Data standardization
- Validation checks
- Parquet optimization

---

## Gold Layer

The Gold layer generates business-ready analytical datasets.

Features:
- Revenue aggregation
- Product analytics
- Category-level KPIs
- Parquet analytics tables
- Optimized reporting datasets

---

# Local Development Setup

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/azure-ecommerce-lakehouse.git
cd azure-ecommerce-lakehouse
```

---

## 2. Create Python Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start Docker Services

```bash
docker compose up -d
```

---

## 5. Verify Containers

```bash
docker ps
```

Expected containers:

- postgres
- kafka
- zookeeper

---

# Environment Variables

The project uses a `.env` file for local configuration.

Example:

```env
AIRFLOW_UID=50000

POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

KAFKA_BROKER=kafka:9092
```

---

## Bronze Layer Features

Implemented features:
- FakeStore API ingestion
- Kafka producer pipeline
- Raw JSON archival
- Timestamp-based storage
- Logging support
- Dockerized Kafka infrastructure

Documentation:
docs/phase-3-bronze-layer.md

---

# Planned Features

- Batch ingestion pipeline
- Kafka streaming pipeline
- Bronze/Silver/Gold Medallion Architecture
- Airflow orchestration
- Data quality validation
- Incremental processing
- Snowflake warehouse integration
- Power BI dashboards
- CI/CD with GitHub Actions
- Infrastructure as Code with Terraform

---

# Git Commit Strategy

This repository follows production-style incremental commits.

Example:

```bash
git commit -m "Add Kafka streaming producer"
git commit -m "Implement Bronze ingestion pipeline"
git commit -m "Add Airflow orchestration DAG"
```

---

# Important Notes

- Never commit `.env` files
- Never commit secrets or credentials
- Never commit large datasets
- Keep commits modular and meaningful
- Update documentation after every major phase

---

# Future Enhancements

- Azure deployment
- Databricks integration
- Real-time analytics
- Data observability
- Monitoring and alerting
- Automated testing
- CDC pipelines
- Streaming analytics

---

# Author

Srinath Reddy Kota

