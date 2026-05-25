import pandas as pd

# ==========================
# EXTRACT
# ==========================
transactions = pd.read_csv("data/postgres_source/transactions.csv")
customers = pd.read_json("data/mongo_source/customers.json")

# Convert amount to numeric
transactions["amount"] = pd.to_numeric(
    transactions["amount"],
    errors="coerce"
)

print("Source Data Loaded")
print("Transactions Shape:", transactions.shape)
print("Customers Shape:", customers.shape)


# ==========================
# SOURCE VALIDATION
# ==========================
print("\n----- SOURCE VALIDATION -----")

# Null values
print("\nTransaction Null Values:")
print(transactions.isnull().sum())

print("\nCustomer Null Values:")
print(customers.isnull().sum())

# Duplicate check
print("\nDuplicate Transaction IDs:")
print(transactions["transaction_id"].duplicated().sum())

print("\nDuplicate Customer IDs:")
print(customers["customer_id"].duplicated().sum())

# Missing join key
print("\nMissing customer_id in Transactions:")
print(transactions["customer_id"].isnull().sum())

print("\nMissing customer_id in Customers:")
print(customers["customer_id"].isnull().sum())

# Negative amount check
print("\nNegative Amount Records:")
print((transactions["amount"] < 0).sum())

# Invalid amount after conversion
print("\nInvalid Amount (NaN after conversion):")
print(transactions["amount"].isnull().sum())

# Invalid status check
valid_status = ["Success", "Failed", "Pending"]

invalid_status = transactions[
    ~transactions["status"].isin(valid_status)
]

print("\nInvalid Status Count:")
print(len(invalid_status))

# Row count
print("\nTransaction Rows:")
print(transactions.shape[0])

print("Customer Rows:")
print(customers.shape[0])


# ==========================
# TRANSFORM / MERGE
# ==========================
print("\n----- CREATING MASTER TABLE -----")

master = transactions.merge(
    customers,
    on="customer_id",
    how="left"
)

print("Master Table Created")
print("Master Shape:", master.shape)


# ==========================
# MASTER TABLE VALIDATION
# ==========================
print("\n----- MASTER TABLE VALIDATION -----")

# Nulls after merge
print("\nMaster Null Values:")
print(master.isnull().sum())

# Duplicate transaction_id
print("\nDuplicate transaction_id in Master:")
print(master["transaction_id"].duplicated().sum())

# Missing customer after merge
print("\nMissing customer_name after merge:")
print(master["customer_name"].isnull().sum())

# Failed transactions
print("\nFailed Transactions:")
print((master["status"] == "Failed").sum())

# Pending transactions
print("\nPending Transactions:")
print((master["status"] == "Pending").sum())

# Fraud transactions
print("\nFraud Transactions:")
print((master["fraud_flag"] == "Yes").sum())

# Total amount
print("\nTotal Transaction Amount:")
print(master["amount"].sum())

# Branch-wise transaction count
print("\nBranch Wise Transaction Count:")
print(master["branch"].value_counts())

# Transaction type count
print("\nTransaction Type Count:")
print(master["transaction_type"].value_counts())

# Payment method count
print("\nPayment Method Count:")
print(master["payment_method"].value_counts())


# ==========================
# LOAD
# ==========================
master.to_csv(
    "data/processed/master_transactions.csv",
    index=False
)

print("\nMaster Table Saved Successfully")
print("Path: data/processed/master_transactions.csv")