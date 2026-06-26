import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = master_codes - nav_codes

print("AMFI CODE VALIDATION")

print(f"Total AMFI Codes in fund_master : {len(master_codes)}")
print(f"Total AMFI Codes in nav_history : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI codes in fund_master are present in nav_history.")
else:
    print(f"\nMissing AMFI Codes: {len(missing_codes)}")
    print(sorted(missing_codes))