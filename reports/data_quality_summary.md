# Data Quality Summary - Day 1

## Project

**Mutual Fund Data Analysis**

## Objective

The objective of Day 1 was to ingest all provided datasets, verify their structure and quality, fetch live NAV data, and perform initial validation before further analysis.


## Tasks Completed

* Created the project folder structure.
* Loaded all **10 provided CSV datasets** using Pandas.
* Successfully fetched and stored **live NAV data** for:

  * HDFC Top 100 Direct
  * SBI Bluechip
  * ICICI Bluechip
  * Nippon Large Cap
  * Axis Bluechip
  * Kotak Bluechip
* Verified the **shape**, **data types**, and **sample records** (`head()`) of every dataset.
* Checked each dataset for **missing values**.
* Checked each dataset for **duplicate records**.
* Explored the `fund_master` dataset to identify fund houses, categories, sub-categories, and risk categories.
* Validated AMFI scheme codes against the NAV history dataset.

---

## Data Quality Findings

### Dataset Loading

* All datasets were loaded successfully without any file reading errors.

### Missing Values

* Most datasets contain **no missing values**.
* `04_monthly_sip_inflows.csv` contains **12 missing values** in the `yoy_growth_pct` column.
* These missing values are expected because Year-over-Year growth cannot be calculated for the initial months.

### Duplicate Records

* No duplicate rows were found in any dataset.

### Data Types

* Numeric columns are correctly stored as `int64` or `float64`.
* Date columns are currently stored as strings (`object`) and should be converted to `datetime` format during preprocessing.

### Live NAV Data

* Live NAV data for all required mutual fund schemes was fetched successfully and saved as CSV files.

### AMFI Code Validation

* AMFI scheme codes were successfully validated between the `fund_master` and `nav_history` datasets.

---

## Overall Assessment

The datasets are clean, well-structured, and suitable for further analysis. No major data quality issues were identified apart from the expected missing values in the `yoy_growth_pct` column. The data is ready for preprocessing, exploratory data analysis (EDA), and dashboard development.
