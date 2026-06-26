
**BlueStock Mutual Fund Analysis**

# 1. fund_master (01_fund_master.csv)

| Column             | Data Type | Description                        |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier      |
| fund_house         | Text      | Mutual fund company name           |
| scheme_name        | Text      | Name of the mutual fund scheme     |
| category           | Text      | Fund category (Equity, Debt, etc.) |
| sub_category       | Text      | Detailed fund category             |
| plan               | Text      | Direct or Regular plan             |
| launch_date        | Date      | Scheme launch date                 |
| benchmark          | Text      | Benchmark index                    |
| expense_ratio_pct  | Float     | Annual expense ratio (%)           |
| exit_load_pct      | Float     | Exit load percentage               |
| min_sip_amount     | Integer   | Minimum SIP investment             |
| min_lumpsum_amount | Integer   | Minimum lump sum investment        |
| fund_manager       | Text      | Fund manager name                  |
| risk_category      | Text      | Risk level                         |
| sebi_category_code | Text      | SEBI category code                 |

**Source:** Internal Mutual Fund Master Dataset

---

# 2. nav_history (02_nav_history.csv)

| Column    | Data Type | Description             |
| --------- | --------- | ----------------------- |
| amfi_code | Integer   | Mutual fund scheme code |
| date      | Date      | NAV date                |
| nav       | Float     | Net Asset Value         |

**Source:** Historical NAV Dataset

---

# 3. aum_by_fund_house (03_aum_by_fund_house.csv)

| Column         | Data Type | Description                          |
| -------------- | --------- | ------------------------------------ |
| date           | Date      | Reporting date                       |
| fund_house     | Text      | Fund house                           |
| aum_lakh_crore | Float     | Assets Under Management (Lakh Crore) |
| aum_crore      | Integer   | Assets Under Management (Crore)      |
| num_schemes    | Integer   | Number of schemes                    |

**Source:** AMFI Industry Data

---

# 4. monthly_sip_inflows (04_monthly_sip_inflows.csv)

| Column                    | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | Text      | Reporting month                  |
| sip_inflow_crore          | Integer   | Monthly SIP inflow               |
| active_sip_accounts_crore | Float     | Active SIP accounts              |
| new_sip_accounts_lakh     | Float     | Newly opened SIP accounts        |
| sip_aum_lakh_crore        | Float     | SIP Assets Under Management      |
| yoy_growth_pct            | Float     | Year-over-Year growth percentage |

**Source:** SIP Industry Reports

---

# 5. category_inflows (05_category_inflows.csv)

| Column           | Data Type | Description          |
| ---------------- | --------- | -------------------- |
| month            | Text      | Reporting month      |
| category         | Text      | Mutual fund category |
| net_inflow_crore | Float     | Net inflow amount    |

**Source:** Category-wise Fund Flow Data

---

# 6. industry_folio_count (06_industry_folio_count.csv)

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

**Source:** Industry Statistics

---

# 7. scheme_performance (07_scheme_performance.csv)

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Mutual fund scheme code       |
| scheme_name        | Text      | Scheme name                   |
| fund_house         | Text      | Fund house                    |
| category           | Text      | Fund category                 |
| plan               | Text      | Scheme plan                   |
| return_1yr_pct     | Float     | 1-year return (%)             |
| return_3yr_pct     | Float     | 3-year return (%)             |
| return_5yr_pct     | Float     | 5-year return (%)             |
| benchmark_3yr_pct  | Float     | Benchmark return              |
| alpha              | Float     | Alpha                         |
| beta               | Float     | Beta                          |
| sharpe_ratio       | Float     | Sharpe Ratio                  |
| sortino_ratio      | Float     | Sortino Ratio                 |
| std_dev_ann_pct    | Float     | Annualized Standard Deviation |
| max_drawdown_pct   | Float     | Maximum Drawdown              |
| aum_crore          | Integer   | Assets Under Management       |
| expense_ratio_pct  | Float     | Expense Ratio                 |
| morningstar_rating | Integer   | Morningstar Rating            |
| risk_grade         | Text      | Risk Grade                    |

**Source:** Scheme Performance Dataset

---

# 8. investor_transactions (08_investor_transactions.csv)

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | Text      | Investor ID                |
| transaction_date   | Date      | Transaction date           |
| amfi_code          | Integer   | Mutual fund scheme code    |
| transaction_type   | Text      | SIP, Lumpsum or Redemption |
| amount_inr         | Integer   | Transaction amount         |
| state              | Text      | Investor state             |
| city               | Text      | Investor city              |
| city_tier          | Text      | City tier                  |
| age_group          | Text      | Investor age group         |
| gender             | Text      | Investor gender            |
| annual_income_lakh | Float     | Annual income              |
| payment_mode       | Text      | Payment method             |
| kyc_status         | Text      | KYC verification status    |

**Source:** Investor Transaction Dataset

---

# 9. portfolio_holdings (09_portfolio_holdings.csv)

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Mutual fund scheme code  |
| stock_symbol      | Text      | Stock symbol             |
| stock_name        | Text      | Company name             |
| sector            | Text      | Business sector          |
| weight_pct        | Float     | Portfolio weight (%)     |
| market_value_cr   | Float     | Market value             |
| current_price_inr | Float     | Current stock price      |
| portfolio_date    | Date      | Portfolio reporting date |

**Source:** Portfolio Holdings Dataset

---

# 10. benchmark_indices (10_benchmark_indices.csv)

| Column      | Data Type | Description         |
| ----------- | --------- | ------------------- |
| date        | Date      | Trading date        |
| index_name  | Text      | Benchmark index     |
| close_value | Float     | Closing index value |

**Source:** Benchmark Index Dataset

---

# Summary

* Total datasets documented: **10**
* All columns include data types and business definitions.
* Source references have been provided for every dataset.
* This document serves as the metadata reference for the BlueStock Mutual Fund Analysis project.
