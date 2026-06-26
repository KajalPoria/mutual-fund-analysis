import pandas as pd

print("Cleaning NAV History Dataset")

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print(f"\nOriginal Shape: {df.shape}")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI Code and Date
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicate rows
duplicates = df.duplicated().sum()

print(f"Duplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# Forward fill missing NAV values
missing_before = df["nav"].isnull().sum()

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

missing_after = df["nav"].isnull().sum()

print(f"Missing NAV Before: {missing_before}")
print(f"Missing NAV After : {missing_after}")

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print(f"Invalid NAV Records: {len(invalid_nav)}")

# Remove invalid NAV values if any
df = df[df["nav"] > 0]


# Save cleaned dataset

output_path = "data/processed/02_nav_history_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")
print(f"Saved to: {output_path}")

print(f"\nFinal Shape: {df.shape}")

print("\nCleaning Completed Successfully.")