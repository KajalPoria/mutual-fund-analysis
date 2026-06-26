import pandas as pd

print("Cleaning Investor Transactions Dataset")

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(f"\nOriginal Shape: {df.shape}")


# Convert transaction_date to datetime

df["transaction_date"] = pd.to_datetime(df["transaction_date"])


# Remove duplicate rows

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# Standardize Transaction Types

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

print("\nUnique Transaction Types:")
print(df["transaction_type"].unique())

# Validate Amount
invalid_amount = (df["amount_inr"] <= 0).sum()

print(f"\nInvalid Amount Records: {invalid_amount}")

df = df[df["amount_inr"] > 0]

# Validate KYC Status

valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print(f"Invalid KYC Status Records: {len(invalid_kyc)}")

# Save cleaned dataset

output_path = "data/processed/08_investor_transactions_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")
print(f"Saved to: {output_path}")

print(f"\nFinal Shape: {df.shape}")

print("\nCleaning Completed Successfully.")