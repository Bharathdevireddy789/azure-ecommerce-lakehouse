# Phase 3 — Bronze Layer Ingestion Pipeline

## Objective

The goal of this phase is to build the Bronze layer of the lakehouse architecture.

The Bronze layer is responsible for ingesting raw data from external systems and storing it in its original format for downstream processing.

---

# Architecture

FakeStore API → Python Ingestion → Kafka → Raw JSON Storage

---

# Components Implemented

## 1. API Ingestion

Data is fetched from the FakeStore API using Python requests.

Source:
https://fakestoreapi.com/products

Implemented in:

spark/bronze/ingest_api.py

---

## 2. Raw Data Archival

Raw API responses are stored as timestamped JSON files.

Benefits:
- historical tracking
- replay capability
- debugging support
- immutable raw layer

Storage path:

data/raw/products/

Example file:

products_20260513_183000.json

---

## 3. Kafka Producer

Fetched product records are streamed into a Kafka topic named:

orders

Implemented in:

spark/bronze/kafka_producer.py

This simulates real-time event ingestion architecture commonly used in production systems.

---

## 4. Logging

Basic logging support was added for:
- ingestion status
- API activity
- operational visibility

Implemented in:

spark/bronze/utils.py

---

# Folder Structure

spark/
└── bronze/
    ├── ingest_api.py
    ├── kafka_producer.py
    ├── save_raw_data.py
    └── utils.py

---

# Technologies Used

- Python
- Kafka
- Docker
- Requests library
- JSON storage

---

# Key Learning Outcomes

- Building API ingestion pipelines
- Streaming records into Kafka
- Designing Bronze/raw storage layers
- Handling timestamped ingestion
- Organizing modular ETL code
- Using Dockerized infrastructure

---

# Future Improvements

- Schema validation
- Retry mechanisms
- Dead-letter queue support
- Incremental ingestion
- Partitioned storage
- Cloud storage migration to Azure Data Lake

---

# Status

✅ Completed