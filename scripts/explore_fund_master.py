import pandas as pd

# Load fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("FUND MASTER DATA EXPLORATION")

# Fund Houses
fund_houses = sorted(df["fund_house"].unique())
print(f"\nTotal Fund Houses: {len(fund_houses)}")
print(fund_houses)

# Categories
categories = sorted(df["category"].unique())
print(f"\nTotal Categories: {len(categories)}")
print(categories)

# Sub Categories
sub_categories = sorted(df["sub_category"].unique())
print(f"\nTotal Sub-Categories: {len(sub_categories)}")
print(sub_categories)

# Risk Categories
risk_categories = sorted(df["risk_category"].unique())
print(f"\nTotal Risk Categories: {len(risk_categories)}")
print(risk_categories)

print("\nExploration completed successfully.")