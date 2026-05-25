## EXTRACTING THE CSV FILE 
## FIRST STEP OF ETL

import pandas as pd

# PostgreSQL-style CSV source
transactions = pd.read_csv("data/postgres_source/transactions.csv")

# MongoDB exported source
customers = pd.read_json("data/mongo_source/customers.json")

print("Transactions Shape:", transactions.shape)
print("Customers Shape:", customers.shape)

print(transactions.head())
print(customers.head())