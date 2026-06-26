import requests
import pandas as pd

# AMFI Scheme Codes
scheme_codes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{scheme_name}.csv"
        nav_df.to_csv(file_path, index=False)

        print(f"{scheme_name} saved successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {scheme_name}: {e}")