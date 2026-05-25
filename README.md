# Master Table Data Quality Pipeline

## Project Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline that integrates data from PostgreSQL and MongoDB to create a master table for data validation and quality checks.

The project focuses on:
- Data extraction
- Data transformation
- Master table creation
- Data validation
- Data quality checks
- Great Expectations validation
- MongoDB query validation

---

## Tech Stack
- Python
- Pandas
- PostgreSQL (CSV source simulation)
- MongoDB
- Great Expectations
- VS Code

---

## Project Structure

```bash
MASTER_TABLE_PROJECT/
│
├── data/
│   ├── mongo_source/
│   │   └── customers.json
│   │
│   ├── postgres_source/
│   │   └── transactions.csv
│   │
│   └── processed/
│       └── master_transactions.csv
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── great_expectation_check.py
│   ├── customervalidation.mongodb.js
│   └── master_table.mongodb.js
│
├── requirements.txt
└── README.md
```

---

## Workflow

### 1. Extract
Load source data from:
- PostgreSQL simulated CSV (`transactions.csv`)
- MongoDB JSON (`customers.json`)

### 2. Transform
- Clean missing values
- Check duplicates
- Convert data types
- Merge source datasets

### 3. Create Master Table
Join both datasets using:
- `customer_id`

Output:
- `master_transactions.csv`

### 4. Validation
Check:
- Null values
- Duplicate IDs
- Negative transaction amount
- Invalid status
- Fraud transactions
- Missing customer records

### 5. Great Expectations
Data quality rules:
- Unique transaction_id
- Non-null transaction_id
- Non-null customer_id
- Amount >= 0
- Valid status
- Valid fraud_flag
- Non-null customer_name

### 6. MongoDB Validation
Validation using MongoDB shell queries:
- Count customers
- High risk customers
- Pending KYC
- Account type analysis
- Aggregation queries

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run ETL Transform
```bash
python scripts/transform.py
```

### Run Validation
```bash
python scripts/validate.py
```

### Run Great Expectations
```bash
python scripts/great_expectation_check.py
```

---

## Key Features
- ETL pipeline
- Hybrid data source integration
- PostgreSQL + MongoDB
- Master table generation
- Data quality checks
- Great Expectations validation
- Fraud detection checks
- Business rule validation

---

## Learning Outcome
This project helped practice:
- ETL concepts
- Data cleaning
- Data transformation
- Master table creation
- Data quality validation
- Great Expectations
- MongoDB queries
- Real-world data engineering workflow

---

## Author
**Aadarsh Kumar Singh**