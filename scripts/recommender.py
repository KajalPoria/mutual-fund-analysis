"""
Mutual Fund Recommendation System
---------------------------------
Recommends the top 3 mutual funds based on
Sharpe Ratio within the selected risk category.
"""

from pathlib import Path
import pandas as pd

# Load Performance Dataset

DATA = Path("../data/processed")

performance = pd.read_csv(
    DATA / "07_scheme_performance_cleaned.csv"
)
print("\nColumns in dataset:\n")
print(performance.columns.tolist())

print("\nUnique Risk Grades:")
print(performance["risk_grade"].unique())


# Risk Mapping

risk_mapping = {
    "Low": ["Low", "Low to Moderate"],
    "Moderate": ["Moderate", "Moderately High"],
    "High": ["High", "Very High"]
}

# Recommendation Function

def recommend_funds(risk_appetite):

    if risk_appetite not in risk_mapping:
        raise ValueError(
            "Choose from: Low, Moderate, High"
        )

    filtered = performance[
        performance["risk_grade"].isin(
            risk_mapping[risk_appetite]
        )
    ]

    recommendations = (
        filtered
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]


# Example

if __name__ == "__main__":

    risk = input(
        "Enter Risk Appetite (Low / Moderate / High): "
    )

    print("\nRecommended Mutual Funds\n")

    print(
        recommend_funds(risk)
    )