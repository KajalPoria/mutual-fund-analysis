import pandas as pd
from sqlalchemy import create_engine

print("Loading Cleaned Data into SQLite Database")

# Create SQLite Database

engine = create_engine("sqlite:///bluestock_mf.db")

print("\nDatabase created successfully.")

# Load CSV Files

files = {

    "dim_fund": "data/raw/01_fund_master.csv",

    "fact_nav": "data/processed/02_nav_history_cleaned.csv",

    "fact_aum": "data/raw/03_aum_by_fund_house.csv",

    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",

    "fact_performance": "data/processed/07_scheme_performance_cleaned.csv",

    "fact_transactions": "data/processed/08_investor_transactions_cleaned.csv"

}

# Load Tables

for table_name, file_path in files.items():

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully.")
    print(f"Rows Inserted: {len(df)}")

print("\nAll datasets loaded successfully!")

# Verify Row Counts

print("\nVerifying Row Counts...\n")

for table_name in files.keys():

    count = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM {table_name}",
        engine
    )

    print(f"{table_name}: {count.iloc[0]['total']} rows")

print("\nSQLite Database Ready.")