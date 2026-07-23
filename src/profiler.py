"""
Dataset profiling module.

This module provides a DatasetProfiler class for generating
basic dataset statistics and quality information.
"""

from __future__ import annotations

import pandas as pd


class DatasetProfiler:
    """
    Generate summary information for a pandas DataFrame.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def shape(self):
        return self.df.shape

    def rows(self):
        return self.df.shape[0]

    def columns(self):
        return self.df.shape[1]

    def dtypes(self):
        return self.df.dtypes

    def missing_values(self):
        return self.df.isnull().sum()

    def missing_percentage(self):
        return (
            self.df.isnull().mean() * 100
        ).round(2)

    def duplicate_rows(self):
        return self.df.duplicated().sum()

    def numeric_columns(self):
        return (
            self.df.select_dtypes(include="number")
            .columns.tolist()
        )

    def categorical_columns(self):
        return (
            self.df.select_dtypes(exclude="number")
            .columns.tolist()
        )

    def memory_usage(self):
        return round(
            self.df.memory_usage(deep=True).sum()
            / 1024,
            2,
        )
    
    def quality_report(self):
             """
             Generate an overall data quality report.
             """
    
             missing_pct = (
                self.df.isnull().mean().mean() * 100
             )
    
             duplicate_pct = (
                 self.df.duplicated().mean() * 100
             )
    
             score = 100
             score -= missing_pct * 0.5
             score -= duplicate_pct * 0.3
    
             score = round(max(score, 0), 2)
    
             if score >= 90:
                grade = "Excellent"
             elif score >= 80:
                grade = "Good"
             elif score >= 70:
                grade = "Fair"
             elif score >= 60:
                grade = "Poor"
             else:
                grade = "Critical"
    
             return {
               "Score": score,
               "Grade": grade,
               "Missing (%)": round(missing_pct, 2),
               "Duplicate (%)": round(duplicate_pct, 2),
             }
    