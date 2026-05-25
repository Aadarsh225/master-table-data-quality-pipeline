import pandas as pd

# LOAD MASTER TABLE
master = pd.read_csv("data/processed/master_transactions.csv")

print("----MASTER TABLE VALIDATION----")

# ==========================
# BASIC CHECKS
# ==========================
print("\nTotal Rows:")
print(master.shape[0])

print("\nTotal Columns:")
print(master.shape[1])

print("\nColumn Names:")
print(master.columns)

# ==========================
# NULL VALUE CHECK
# ==========================
print("\nNULL Values")
print(master.isnull().sum())



# ==========================
# DUPLICATE CHECKS
# ==========================
print("\nDuplicate transaction_id:")
print(master["transaction_id"].duplicated().sum())

print("\nDuplicate customer_id:")
print(master["customer_id"].duplicated().sum())

# ==========================
# DATA QUALITY CHECKS
# ==========================
print("\nNegative Amount Records:")
print((master["amount"] < 0).sum())

print("\nMissing customer_name:")
print(master["customer_name"].isnull().sum())

print("\nMissing city:")
print(master["city"].isnull().sum())

# ==========================
# BUSINESS RULE CHECK
# ==========================
print("\nFailed Transaction")
print((master["status"]=="Failed").sum())

print("\nPending Transaction")
print((master["status"]=="Pending").sum())

print("\nFraud Transaction")
print((master["fraud_flag"]=="Yes").sum())

# ==========================
# Analysis
# ==========================
print("\nBranch wise transaction Count")
print(master["branch"].value_counts())

print("\nPayment Method Count:")
print(master["payment_method"].value_counts())

print("\nTransaction Type Count:")
print(master["transaction_type"].value_counts())

print("\nRisk Level Count:")
print(master["risk_level"].value_counts())

print("\nKYC Status Count:")
print(master["kyc_status"].value_counts())

# ==========================
# Aggregation
# ==========================

print("\nTotal Transaction Amount:")
print(master["amount"].sum())

print("\nAverage Transaction Amount")
print(master["amount"].mean())

print("\nMaximum Transaction Amount")
print(master["amount"].max())

print("\nMinimum Transaction Amount")
print(master["amount"].min())

negative_amount = master[master["amount"] < 0]

print("\nNegative Amount Records:")
print(negative_amount)

master["amount"] = master["amount"].abs()


# ==========================
# DATE ANALYSIS
# ==========================
print("\nTransactions Per Day:")
print(master["transaction_date"].value_counts().sort_index())

print("\nTransactions Per Branch (Amount Sum):")
print(master.groupby("branch")["amount"].sum())