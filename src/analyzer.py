"""
Dataset analysis module.

Provides analytical summaries for a pandas DataFrame.
"""

from __future__ import annotations

import pandas as pd


class DatasetAnalyzer:
    """
    Perform analytical operations on a dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def missing_summary(self):
        """
        Return missing value count and percentage
        for each column.
        """

        missing = self.df.isna().sum()

        percentage = (
            self.df.isna().mean() * 100
        ).round(2)

        summary = pd.DataFrame({
            "Missing Values": missing,
            "Percentage (%)": percentage
        })

        return summary[summary["Missing Values"] > 0]\
            .sort_values(
                by="Missing Values",
                ascending=False
            )

    def duplicate_summary(self):
        """
        Return duplicate row statistics.
        """

        duplicates = int(self.df.duplicated().sum())

        return {
            "Duplicate Rows": duplicates,
            "Duplicate Percentage": round(
                duplicates / len(self.df) * 100,
                2
            )
        }

    def numeric_summary(self):
        """
        Summary statistics of numeric columns.
        """

        return self.df.describe().T

    def categorical_summary(self):
        """
        Summary statistics of categorical columns.
        """

        return self.df.describe(
            include="object"
        ).T

    def correlation_matrix(self):
        """
        Correlation matrix of numeric columns.
        """

        return self.df.corr(
            numeric_only=True
        )