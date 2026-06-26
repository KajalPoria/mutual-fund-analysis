import pandas as pd

print("Cleaning Scheme Performance Dataset")

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(f"\nOriginal Shape: {df.shape}")

# Convert return columns to numeric

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

for column in return_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check Missing Values

print("\nMissing Values:")
print(df[return_columns].isnull().sum())

# Expense Ratio Validation

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"\nInvalid Expense Ratio Records: {len(invalid_expense)}")

# -------------------------------------------------
# Flag Return Anomalies
# -------------------------------------------------

anomalies = df[
    (df["return_1yr_pct"] < -100) |
    (df["return_1yr_pct"] > 200)
]

print(f"Return Anomalies Found: {len(anomalies)}")

# -------------------------------------------------
# Remove Duplicate Rows
# -------------------------------------------------

duplicates = df.duplicated().sum()

print(f"Duplicate Rows: {duplicates}")

df = df.drop_duplicates()

# Save cleaned dataset
output_path = "data/processed/07_scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")

print(f"Saved to: {output_path}")

print(f"\nFinal Shape: {df.shape}")

print("\nCleaning Completed Successfully.")