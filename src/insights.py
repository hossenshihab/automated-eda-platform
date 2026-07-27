"""
Automatic insight generation module.

Generates human-readable insights and
recommendations from a dataset.
"""

import pandas as pd
import numpy as np


class DatasetInsights:

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    def dataset_summary(self):
        """
        Basic dataset information.
        """

        return {
            "Rows": self.df.shape[0],
            "Columns": self.df.shape[1],
            "Missing Values": int(self.df.isna().sum().sum()),
            "Duplicate Rows": int(self.df.duplicated().sum()),
        }

    def missing_value_insights(self):
        """
        Analyze missing values and provide recommendations.
        """

        missing = self.df.isnull().sum()
        missing_percent = (
            self.df.isnull().mean() * 100
        ).round(2)

        insights = []

        for column in self.df.columns:

            if missing[column] == 0:
                continue

            pct = missing_percent[column]

            if pct > 50:
                recommendation = (
                    "Consider dropping this column "
                    "(more than 50% missing)."
                )

            elif pd.api.types.is_numeric_dtype(
                self.df[column]
            ):
                recommendation = (
                    "Fill missing values using median."
                )

            else:
                recommendation = (
                    "Fill missing values using mode."
                )

            insights.append({
                "Column": column,
                "Missing Count": int(missing[column]),
                "Missing (%)": float(pct),
                "Recommendation": recommendation,
            })

        return insights

    def duplicate_insights(self):
        """
        Analyze duplicate rows.
        """

        duplicates = int(
            self.df.duplicated().sum()
        )

        if duplicates == 0:
            recommendation = (
                "No duplicate rows detected."
            )
        else:
            recommendation = (
                "Remove duplicate rows before analysis."
            )

        return {
            "Duplicate Rows": duplicates,
            "Recommendation": recommendation,
        }

    def outlier_insights(self):
        """
        Detect outliers using the IQR method.
        """

        insights = []

        numeric_columns = self.df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            outliers = self.df[
                (self.df[column] < lower)
                | (self.df[column] > upper)
            ]

            insights.append({
                "Column": column,
                "Outliers": len(outliers),
                "Recommendation":
                    "Review or treat outliers."
                    if len(outliers) > 0
                    else "No significant outliers."
            })

        return insights

    def correlation_insights(
        self,
        threshold: float = 0.8,
    ):
        """
        Detect highly correlated numeric features.
        """

        corr = self.df.corr(numeric_only=True).abs()

        insights = []

        for i in range(len(corr.columns)):
            for j in range(i + 1, len(corr.columns)):

                value = corr.iloc[i, j]

                if value >= threshold:

                    insights.append({
                        "Feature 1": corr.columns[i],
                        "Feature 2": corr.columns[j],
                        "Correlation": round(value, 2),
                        "Recommendation":
                            "Consider removing one of these features to reduce multicollinearity."
                    })

        if len(insights) == 0:

            return [{
                "Recommendation":
                    "No highly correlated features detected."
            }]

        return insights

    def overall_recommendation(self):
        """
        Generate an overall recommendation for the dataset.
        """

        missing_pct = (
            self.df.isnull().mean().mean() * 100
        )

        duplicate_rows = self.df.duplicated().sum()

        numeric_df = self.df.select_dtypes(include="number")

        high_corr = 0

        if numeric_df.shape[1] > 1:

            corr = numeric_df.corr().abs()

            for i in range(len(corr.columns)):
                for j in range(i + 1, len(corr.columns)):
                    if corr.iloc[i, j] >= 0.8:
                        high_corr += 1

        score = 100

        score -= missing_pct * 0.5
        score -= duplicate_rows * 0.2
        score -= high_corr * 5

        score = float(max(0, round(score, 2)))

        if score >= 90:
            readiness = "Excellent"
        elif score >= 80:
            readiness = "Good"
        elif score >= 70:
            readiness = "Fair"
        elif score >= 60:
            readiness = "Poor"
        else:
            readiness = "Critical"

        recommendations = []
        
        if missing_pct > 0:
            recommendations.append(
                "Handle missing values before model training."
            )

        if duplicate_rows > 0:
            recommendations.append(
                "Remove duplicate rows."
            )

        if high_corr > 0:
            recommendations.append(
                "Review highly correlated features."
            )

        if (
            missing_pct == 0
            and duplicate_rows == 0
            and high_corr == 0
        ):
            recommendations.append(
                "Dataset is ready for machine learning."
            )

        return {
            "Readiness Score": score,
            "Status": readiness,
            "Recommendations": recommendations,
        }

    def generate_report(self):
        """
        Generate a complete insight report.
        """

        return {
            "Dataset Summary":
                self.dataset_summary(),

            "Missing Value Insights":
                self.missing_value_insights(),

            "Duplicate Insights":
                self.duplicate_insights(),

            "Outlier Insights":
                self.outlier_insights(),

            "Correlation Insights":
                self.correlation_insights(),

            "Overall Recommendation":
                self.overall_recommendation(),
        }



    