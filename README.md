# 📊 Mutual Fund Analytics Capstone Project

## End-to-End Financial Data Analytics & Business Intelligence Solution

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Data%20Processing-013243?logo=numpy)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 👩‍💻 Project Information

| **Field** | **Details** |
|---|---|
| **Project** | Mutual Fund Analytics Capstone Project |
| **Organization** | Bluestock Fintech |
| **Author** | Kajal Poria |
| **Project Type** | Internship Capstone Project |
| **Domain** | Financial Data Analytics |
| **Focus Areas** | Data Engineering, Financial Analytics, Business Intelligence |

---

## 📌 Project Overview

The **Mutual Fund Analytics Capstone Project** is an end-to-end financial analytics solution designed to process, analyze, and visualize mutual fund data.

The project combines **data engineering, exploratory data analysis, financial performance evaluation, risk analytics, and business intelligence** into a unified analytical workflow.

Raw mutual fund datasets are collected from multiple sources, cleaned and validated using Python, structured into an SQLite database, analyzed using financial metrics, and transformed into interactive **Power BI dashboards**.

The project also includes advanced analytics such as:

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Analysis
- Herfindahl-Hirschman Index (HHI)
- Risk-based Mutual Fund Recommendation System

---

## 🎯 Project Objectives

The primary objectives of this project are:

- Build an automated ETL pipeline for mutual fund datasets
- Clean and validate raw financial data
- Store processed datasets in SQLite
- Perform exploratory data analysis
- Analyze NAV, AUM, SIP, and investor trends
- Calculate industry-standard financial performance metrics
- Evaluate investment risk
- Develop an interactive Power BI dashboard
- Perform advanced investment analytics
- Generate actionable business insights
- Develop a risk-based mutual fund recommendation system

---

## 🏗️ Project Architecture

Raw CSV Files + Live NAV Data
              │
              ▼
      Data Ingestion
              │
              ▼
      Data Validation
              │
              ▼
       Data Cleaning
              │
              ▼
      SQLite Database
              │
              ▼
 Exploratory Data Analysis
              │
              ▼
   Financial Performance
          Analytics
              │
              ▼
      Power BI Dashboard
              │
              ▼
     Advanced Analytics
              │
              ▼
      Business Insights

📂 Dataset Description
The project utilizes 10 major datasets covering different aspects of the mutual fund industry.
Dataset	Description
Fund Master	Scheme details and classifications
NAV History	Daily NAV records
AUM by Fund House	Assets Under Management by fund house
Monthly SIP Inflows	Monthly investment trends
Category Inflows	Investment category analysis
Industry Folio Count	Number of investor accounts
Scheme Performance	Historical scheme returns
Investor Transactions	Individual investment records
Portfolio Holdings	Sector and portfolio allocation
Benchmark Indices	NIFTY 50 and NIFTY 100 benchmark data


🛠️ Technology Stack
Programming Language
- Python
Python Libraries
- Pandas
- NumPy
- Matplotlib
- Plotly
- SciPy
- SQLAlchemy
- Requests
Database
- SQLite
Visualization & Business Intelligence
- Microsoft Power BI
- Matplotlib
- Plotly
Development Environment
- Jupyter Notebook
- Visual Studio Code
🔄 ETL Pipeline
The project follows an Extract → Transform → Load architecture.
1. Extract
Data is collected from:
- Multiple CSV datasets
- Historical financial datasets
- Live NAV API sources
2. Transform
The raw data is processed through:
- Missing value handling
- Duplicate removal
- Date standardization
- Data type conversion
- Numeric validation
- Invalid record removal
- Data consistency checks
3. Load
The cleaned datasets are loaded into an SQLite relational database designed for efficient analytical queries.
🧹 Data Cleaning & Validation
NAV History
The following preprocessing operations were performed:
- Removed duplicate records
- Converted dates into standardized formats
- Validated NAV values
- Handled missing observations
- Applied appropriate missing-value handling
Scheme Performance
- Validated numeric columns
- Checked return values
- Validated expense ratio information
- Standardized scheme identifiers
Investor Transactions
- Standardized transaction records
- Removed invalid transaction amounts
- Validated transaction dates
- Checked investor-related fields
🗄️ SQLite Database Design
A structured relational database was created using SQLite.
Dimension Tables
dim_fund
dim_date

Fact Tables
fact_nav
fact_performance
fact_transactions
fact_aum

Database Architecture
                    ┌──────────────┐
                    │   dim_fund   │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   ┌────────────┐  ┌───────────────┐  ┌────────────┐
   │  fact_nav  │  │fact_performance│  │  fact_aum  │
   └────────────┘  └───────────────┘  └────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │fact_transactions │
                  └──────────────────┘

This database structure enables efficient analytical queries and provides a clean foundation for Power BI reporting.
📈 Exploratory Data Analysis
Exploratory Data Analysis was performed to identify trends, patterns, and relationships within the mutual fund ecosystem.
Major Analyses
- NAV trend analysis
- AUM growth analysis
- SIP inflow trends
- Category-wise investment analysis
- Investor demographics
- Correlation analysis
- Sector allocation
- Fund house comparison
- Scheme performance comparison
Key Visualizations
- NAV Trend Charts
- AUM Growth Charts
- SIP Inflow Time Series
- Correlation Heatmaps
- Investor Demographic Charts
- Fund House Comparison
- Sector Allocation Charts
📊 Financial Performance Analytics
Multiple financial metrics were implemented to evaluate mutual fund performance.
Daily Returns
Daily return measures the percentage change in NAV between two consecutive trading days.
Daily Return = (Current NAV - Previous NAV) / Previous NAV

CAGR
Compound Annual Growth Rate measures the annualized growth of an investment over a specific period.
CAGR = (Ending Value / Beginning Value)^(1 / Years) - 1

Sharpe Ratio
The Sharpe Ratio measures risk-adjusted return relative to total volatility.
Sharpe Ratio = (Portfolio Return - Risk Free Rate) / Standard Deviation

A higher Sharpe Ratio generally indicates better risk-adjusted performance.
Sortino Ratio
The Sortino Ratio focuses specifically on downside volatility.
Sortino Ratio = (Return - Target Return) / Downside Deviation

Alpha
Alpha measures the excess return generated by a fund compared with its expected benchmark return.
Beta
Beta measures the sensitivity of a fund's returns to market movements.
Beta = Covariance(Fund, Market) / Variance(Market)

Maximum Drawdown
Maximum Drawdown measures the largest decline from a historical peak to a subsequent trough.
Maximum Drawdown =
(Trough Value - Peak Value) / Peak Value

Fund Scorecard
A comprehensive fund scorecard was developed by combining multiple performance and risk indicators to enable easier comparison between schemes.
⚠️ Risk Analytics
The project includes advanced downside-risk analysis.
Implemented Metrics
- Historical Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Maximum Drawdown
- Downside Deviation
- Rolling Sharpe Ratio
- Portfolio Concentration
These metrics provide a more comprehensive understanding of investment risk beyond traditional return-based analysis.
📊 Power BI Dashboard
An interactive Power BI dashboard was developed to communicate analytical findings effectively.
Dashboard Pages
1. Industry Overview
Provides a high-level overview of:
- Total AUM
- SIP Inflows
- Folio Count
- Number of Schemes
- Fund House Performance
2. Fund Performance
Includes:
- NAV Trends
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
3. NAV Analysis
Provides detailed historical NAV analysis and scheme-level comparisons.
4. Investor Analytics
Analyzes:
- Investor Transactions
- Investor Behavior
- Folio Trends
- Cohort Performance
- SIP Continuity
5. SIP & Market Trends
Visualizes:
- SIP Inflows
- Category-wise Flows
- Market Trends
- Investment Patterns
Dashboard Features
- Interactive slicers
- Dynamic filters
- Drill-through
- KPI cards
- Interactive charts
- Cross-filtering
- Scheme-level analysis
🧠 Advanced Analytics
The project goes beyond traditional descriptive analytics through several advanced techniques.
Value at Risk (VaR)
VaR estimates the potential loss of an investment portfolio over a specified time period and confidence level.
Conditional Value at Risk (CVaR)
CVaR measures the expected loss in the worst-performing portion of the return distribution beyond the VaR threshold.
Rolling Sharpe Ratio
Rolling Sharpe Ratio tracks how risk-adjusted performance changes over time.

This helps identify:
- Strong performance periods
- Weak performance periods
- Increasing risk
- Improving risk-adjusted returns
Investor Cohort Analysis
Investors are grouped based on characteristics such as:
- Investment period
- Transaction behavior
- Investment frequency
This helps identify differences in investor behavior across different cohorts.
SIP Continuity Analysis
SIP continuity analysis measures how consistently investors maintain their systematic investment plans over time.
Herfindahl-Hirschman Index (HHI)
HHI is used to measure portfolio concentration.
HHI = Σ(Market Share²)

A higher HHI indicates greater concentration, while a lower HHI indicates greater diversification.
🤖 Mutual Fund Recommendation System
A risk-based mutual fund recommendation framework was developed to help match funds with different investor risk profiles.
Example Investor Profiles
Conservative
      │
      ▼
Lower Risk Funds
      │
      ▼
Moderate Risk
      │
      ▼
Balanced Funds
      │
      ▼
Aggressive
      │
      ▼
Higher Growth Funds

The recommendation framework considers factors such as:
- Risk level
- Historical returns
- Sharpe Ratio
- Volatility
- Maximum Drawdown
- Fund category
Disclaimer: The recommendations generated by this project are analytical outputs for educational and research purposes and should not be considered financial advice.

💡 Business Insights
The analysis provides several useful insights into mutual fund performance and investor behavior.
Key Observations
- Large-cap funds can provide relatively stable risk-adjusted performance.
- SIP inflows demonstrate long-term investment participation trends.
- Diversified portfolios can reduce concentration risk.
- Rolling Sharpe Ratios help identify changes in risk-adjusted performance.
- Fund performance should be evaluated using multiple metrics rather than returns alone.
- Investor cohort analysis provides insights into investment behavior.
- Risk-based recommendations can simplify the process of comparing mutual funds.
Note: Final business insights should be updated according to the actual results obtained from the project's datasets.

🚧 Challenges Faced
Challenge	Solution
Missing NAV values	Applied appropriate validation and missing-value handling
Duplicate records	Identified and removed duplicate observations
Inconsistent date formats	Standardized dates across datasets
Multiple datasets	Created a structured ETL workflow
Invalid financial values	Applied data validation rules
Complex financial metrics	Implemented financial formulas using Python
Dashboard complexity	Used Power BI slicers and drill-through
Data integration	Designed a structured SQLite database


📁 Project Structure
Mutual-Fund-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_performance_analysis.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── dashboard/
│   └── mutual_fund_dashboard.pbix
│
├── reports/
│   └── final_report.pdf
│
├── requirements.txt
└── README.md

▶️ How to Run the Project
Step 1: Clone the Repository
git clone <your-repository-url>
cd Mutual-Fund-Analytics

Step 2: Create a Virtual Environment
python -m venv venv

Step 3: Activate the Virtual Environment
Windows
venv\Scripts\activate

Linux / macOS
source venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt

Step 5: Launch Jupyter Notebook
jupyter notebook

Step 6: Run the Notebooks
Run the notebooks in the following order:
01. Data Ingestion
        ↓
02. Data Cleaning
        ↓
03. Exploratory Data Analysis
        ↓
04. Performance Analytics
        ↓
05. Advanced Analytics

Step 7: Open the Power BI Dashboard
Open the Power BI file:
dashboard/mutual_fund_dashboard.pbix

Refresh the data connections if required.
📦 Requirements
Create a requirements.txt file containing:
pandas
numpy
matplotlib
plotly
sqlalchemy
scipy
jupyter
requests

Install all dependencies using:
pip install -r requirements.txt

📸 Project Screenshots
Add screenshots of your actual project here.
📊 Power BI Dashboard
Add your Power BI dashboard screenshot here.
📈 NAV Trend Analysis
Add your NAV trend visualization here.
💰 SIP Inflow Analysis
Add your SIP inflow visualization here.
📉 Risk Analytics
Add your risk analytics visualization here.
🔮 Future Scope
The project can be further enhanced with:
- Live NAV data refresh using APIs
- Streamlit-based web application
- Monte Carlo simulation for NAV forecasting
- Markowitz portfolio optimization
- Machine learning-based fund recommendations
- Automated email reporting
- Cloud-based data warehouse
- Scheduled ETL pipelines
- Real-time analytics
- Mobile-friendly analytics dashboard
🏆 Key Skills Demonstrated
This project demonstrates practical experience in:
Data Analytics
- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- Financial Data Analysis
- Data Visualization
Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Plotly
SQL & Database
- SQLite
- SQL Queries
- Database Design
- Data Modeling
- SQLAlchemy
Business Intelligence
- Power BI
- Dashboard Development
- KPI Design
- Interactive Filters
- Drill-through Analysis
- Business Reporting
Financial Analytics
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- VaR
- CVaR
- HHI
📚 References
- Association of Mutual Funds in India (AMFI)
- MFAPI Documentation
- Pandas Documentation
- NumPy Documentation
- SciPy Documentation
- SQLAlchemy Documentation
- Microsoft Power BI Documentation
👩‍💻 Author
Kajal Poria
B.Tech Computer Science Engineering
Areas of Interest
- Data Analytics
- Software Engineering
- Financial Technology
- Business Intelligence
- Data Science
