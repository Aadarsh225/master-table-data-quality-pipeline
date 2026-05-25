import pandas as pd
import great_expectations as gx

# Load master table
df = pd.read_csv("data/processed/master_transactions.csv")

# Context
context = gx.get_context()

# Datasource
datasource = context.data_sources.add_pandas(
    "master_datasource"
)

# Data Asset
data_asset = datasource.add_dataframe_asset(
    name="master_data"
)

# Batch Request
batch_request = data_asset.build_batch_request(
    options={"dataframe": df}
)

# Suite Name
suite_name = "master_validation_suite"

# Create / Update Suite
context.suites.add_or_update(
    gx.ExpectationSuite(
        name=suite_name
    )
)

# Validator
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name
)

print("----- GREAT EXPECTATIONS CHECK -----")

# 1. transaction_id should be unique
print(
    validator.expect_column_values_to_be_unique(
        column="transaction_id"
    )
)

# 2. transaction_id should not be null
print(
    validator.expect_column_values_to_not_be_null(
        column="transaction_id"
    )
)

# 3. customer_id should not be null
print(
    validator.expect_column_values_to_not_be_null(
        column="customer_id"
    )
)

# 4. amount should be >= 0
print(
    validator.expect_column_values_to_be_between(
        column="amount",
        min_value=0
    )
)

# 5. status should be valid
print(
    validator.expect_column_values_to_be_in_set(
        column="status",
        value_set=["Success", "Failed", "Pending"]
    )
)

# 6. fraud_flag should be valid
print(
    validator.expect_column_values_to_be_in_set(
        column="fraud_flag",
        value_set=["Yes", "No"]
    )
)

# 7. customer_name should not be null
print(
    validator.expect_column_values_to_not_be_null(
        column="customer_name"
    )
)

print("\nGreat Expectations Validation Completed")