# Phase 2 — Local Development Environment Setup

## Objective

The goal of Phase 2 is to create a clean, production-style local development environment for the Azure E-Commerce Lakehouse project.

This phase establishes:

- Python virtual environment
- Dependency management
- Docker infrastructure
- Kafka setup
- PostgreSQL setup
- Environment variable management
- Local development workflow

---

# Tools Installed

| Tool | Purpose |
|---|---|
| Python | Core development language |
| Docker | Containerized infrastructure |
| Docker Compose | Multi-container orchestration |
| Kafka | Streaming platform |
| PostgreSQL | Airflow metadata database |
| Git | Version control |

---

# Step 1 — Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## PowerShell Execution Policy Issue

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then retry:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 2 — Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Step 3 — Install Core Dependencies

```bash
pip install pandas pyspark apache-airflow kafka-python psycopg2-binary
```

Freeze dependencies:

```bash
pip freeze > requirements.txt
```

---

# Step 4 — Configure Environment Variables

Create:

```text
.env
```

Add:

```env
AIRFLOW_UID=50000

POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

KAFKA_BROKER=kafka:9092
```

---

# Step 5 — Update .gitignore

```gitignore
venv/
.env
__pycache__/
*.pyc
```

---

# Step 6 — Install Docker Desktop

Install Docker Desktop and verify installation.

Verify:

```bash
docker --version
docker compose version
```

---

# Step 7 — Docker Compose Infrastructure

Create:

```text
docker-compose.yml
```

Configuration:

```yaml
version: '3'

services:

  postgres:
    image: postgres:13
    container_name: airflow_postgres
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    ports:
      - "5432:5432"

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka:latest
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

---

# Step 8 — Start Containers

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

Expected containers:

- airflow_postgres
- kafka
- zookeeper

---

# Step 9 — Kafka Topic Setup

Enter Kafka container:

```bash
docker exec -it kafka bash
```

Create topic:

```bash
kafka-topics --create \
--topic orders \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

Verify:

```bash
kafka-topics --list --bootstrap-server localhost:9092
```

Expected output:

```text
orders
```

---

# Local Infrastructure Overview

| Service | Port |
|---|---|
| PostgreSQL | 5432 |
| Kafka | 9092 |
| Zookeeper | 2181 |

---

# Expected Outcomes

After Phase 2:

- Local development environment operational
- Kafka streaming infrastructure ready
- PostgreSQL database running
- Python dependencies managed
- Docker infrastructure configured
- Repository prepared for ingestion pipeline development

---

# Git Commit Recommendations

```bash
git commit -m "Setup Python virtual environment and dependencies"

git commit -m "Add Docker Compose infrastructure for Kafka and PostgreSQL"

git commit -m "Configure local Kafka development environment"
```

---

# Next Phase

Phase 3 — Bronze Layer Ingestion Pipeline

Planned deliverables:

- FakeStore API ingestion
- Kafka producer
- Raw JSON ingestion
- Bronze storage layer
- Logging and error handling
- Incremental ingestion strategy
````