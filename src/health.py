"""
Dataset health analysis module.

This module evaluates the health of a dataset by checking
for constant columns, empty columns, empty rows,
and high-cardinality columns.
"""

from __future__ import annotations

import pandas as pd

from src.profiler import DatasetProfiler


class DatasetHealth:
    """
    Analyze the overall health of a pandas DataFrame.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
        self.profiler = DatasetProfiler(dataframe)

    def constant_columns(self):
        """
        Return columns containing only one unique value.
        """
        return [
            col
            for col in self.df.columns
            if self.df[col].nunique(dropna=False) == 1
        ]

    def empty_columns(self):
        """
        Return columns where every value is missing.
        """
        return self.df.columns[
            self.df.isna().all()
        ].tolist()

    def empty_rows(self):
        """
        Return the number of completely empty rows.
        """
        return int(self.df.isna().all(axis=1).sum())

    def high_cardinality_columns(self, threshold=50):
        """
        Return columns with more than 'threshold'
        unique values.
        """
        return [
            col
            for col in self.df.columns
            if self.df[col].nunique(dropna=False) > threshold
        ]

    def health_report(self):
        """
        Return a complete dataset health report.
        """

        quality = self.profiler.quality_report()

        return {
            "Rows": self.profiler.rows(),
            "Columns": self.profiler.columns(),
            "Memory (KB)": self.profiler.memory_usage(),
            "Constant Columns": self.constant_columns(),
            "Empty Columns": self.empty_columns(),
            "Empty Rows": self.empty_rows(),
            "High Cardinality Columns": self.high_cardinality_columns(),
            "Quality Score": quality["Score"],
            "Quality Grade": quality["Grade"],
        }