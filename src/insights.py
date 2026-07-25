"""
Automatic insight generation module.

Generates human-readable insights and
recommendations from a dataset.
"""

import pandas as pd
import numpy as np


class InsightGenerator:

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