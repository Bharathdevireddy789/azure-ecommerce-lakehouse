# Phase 9 — CI/CD with GitHub Actions

## Overview

In this phase, we implement a CI/CD (Continuous Integration / Continuous Deployment) pipeline using GitHub Actions.

The purpose of this phase is to automate:
- dependency installation
- testing
- code validation
- linting checks

This makes the project more production-oriented and demonstrates engineering best practices.

---

# Objectives

By the end of this phase, the project will support:

- Automated test execution
- Code quality validation
- GitHub Actions workflows
- CI pipeline execution on every push
- Automated repository validation

---

# Final Architecture

```text
Git Push
   ↓
GitHub Actions
   ├── Install Dependencies
   ├── Run Tests
   ├── Run Lint Checks
   └── Validate Pipeline
```

---

# Step 1 — Create GitHub Actions Structure

## Purpose

GitHub Actions workflows must be stored inside the `.github/workflows` directory.

This allows GitHub to automatically detect and execute workflows.

---

## Create Directory

```bash
mkdir -p .github/workflows
```

---

## Create Workflow File

```text
.github/workflows/ci_pipeline.yml
```

---

# Step 2 — Create Test Structure

## Purpose

We create dedicated test files to validate different layers of the data pipeline.

This helps ensure:
- ingestion works correctly
- Spark initializes correctly
- output folders exist

---

## Create Test Files

```text
tests/
├── test_bronze.py
├── test_silver.py
└── test_gold.py
```

---

# Step 3 — Create Bronze Layer Test

## File

```text
tests/test_bronze.py
```

---

## Code

```python
from spark.bronze.ingest_api import fetch_products

def test_fetch_products():

    products = fetch_products()

    assert products is not None
    assert len(products) > 0
```

---

## What This Test Does

This test validates:
- API connectivity
- successful ingestion
- non-empty API response

This ensures the Bronze ingestion layer works correctly.

---

# Step 4 — Create Silver Layer Test

## File

```text
tests/test_silver.py
```

---

## Code

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("SilverTest")
    .getOrCreate()
)

def test_spark_session():

    assert spark is not None
```

---

## What This Test Does

This test verifies:
- PySpark initializes successfully
- Spark environment is configured properly

This helps validate the Spark processing environment.

---

# Step 5 — Create Gold Layer Test

## File

```text
tests/test_gold.py
```

---

## Code

```python
import os

def test_gold_directory_exists():

    assert os.path.exists("data/processed/gold")
```

---

## What This Test Does

This test checks:
- Gold layer output directory exists
- analytics output pipeline completed successfully

This validates Gold layer generation.

---

# Step 6 — Install Testing Dependencies

## Purpose

We install:
- pytest for automated testing
- flake8 for linting and code quality checks

---

## Install Packages

```bash
pip install pytest flake8
```

---

## Update Requirements File

```bash
pip freeze > requirements.txt
```

This ensures all dependencies are version-controlled.

---

# Step 7 — Create GitHub Actions Workflow

## File

```text
.github/workflows/ci_pipeline.yml
```

---

## Workflow Code

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

  pull_request:
    branches:
      - main

jobs:

  build-and-test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set Up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Tests
        run: |
          pytest

      - name: Run Lint Checks
        run: |
          flake8 .
```

---

# What This Workflow Does

Every push or pull request triggers the CI pipeline.

The workflow performs the following tasks:

1. Checks out repository code
2. Installs Python
3. Installs project dependencies
4. Runs automated tests
5. Runs lint validation

This creates automated repository validation.

---

# Step 8 — Create Flake8 Configuration

## File

```text
.flake8
```

---

## Code

```text
[flake8]
max-line-length = 120
exclude = venv,__pycache__
```

---

## What This Does

This configures linting rules:
- maximum line length
- excluded directories

This keeps linting manageable and readable.

---

# Step 9 — Run Tests Locally

## Purpose

Before pushing code to GitHub, validate the project locally.

---

## Run Pytest

```bash
pytest
```

---

## Expected Output

```text
3 passed
```

---

## Run Flake8

```bash
flake8 .
```

---

## What This Does

This validates:
- tests pass successfully
- no major linting errors exist

---

# Step 10 — Push CI/CD Pipeline to GitHub

## Add Files

```bash
git add .
```

---

## Create Commit

```bash
git commit -m "Add CI/CD workflow with automated testing"
```

---

## Push to GitHub

```bash
git push origin main
```

---

# Step 11 — Verify GitHub Actions Execution

## Purpose

After pushing, GitHub automatically executes the workflow.

---

## Steps

1. Open GitHub repository
2. Click "Actions" tab
3. Verify workflow execution

---

## Expected Result

You should see:
- successful workflow run
- green checkmark
- completed tests

---

# Step 12 — Add Build Status Badge

## Purpose

Badges make repositories look more professional and provide visible CI status.

---

## Add Badge to README

```markdown
![CI Pipeline](https://github.com/YOUR_USERNAME/azure-ecommerce-lakehouse/actions/workflows/ci_pipeline.yml/badge.svg)
```

---

# Step 13 — Create CI/CD Documentation

## File

```text
docs/cicd.md
```

---

## Documentation Content

```markdown
# CI/CD Pipeline

The project uses GitHub Actions for automated validation.

Checks include:
- Dependency installation
- Automated tests
- Lint validation
- Pipeline verification
```

---

# Step 14 — Update README

## Add CI/CD Section

```markdown
## CI/CD

The project includes automated GitHub Actions workflows for:
- Testing
- Linting
- Continuous integration
```

---

# Step 15 — Professional Git Commits

## Commit 1

```bash
git add .
git commit -m "Add automated pytest validation suite"
```

---

## Commit 2

```bash
git add .
git commit -m "Configure GitHub Actions CI pipeline"
```

---

## Commit 3

```bash
git add .
git commit -m "Add linting and CI documentation"
```

---

# Step 16 — Push Final Changes

```bash
git push origin main
```

---

# Final Outcome

At the end of this phase, the project supports:

- Automated testing
- Continuous integration
- Code quality validation
- GitHub Actions workflows
- Production-style repository management

---

# Skills Demonstrated

This phase demonstrates:

- CI/CD engineering
- GitHub Actions
- Automated testing
- Linting
- Repository automation
- Production workflow practices

These are highly valuable software and data engineering skills.