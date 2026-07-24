import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


class DataCleaner:
    """
    A reusable class for common data cleaning tasks.
    """

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    # -------------------------
    # Missing Values
    # -------------------------

    def fill_missing_mean(self):
        """
        Fill numeric missing values with column mean.
        """
        numeric_cols = self.df.select_dtypes(include="number").columns

        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(
                self.df[col].mean()
            )

        return self.df

    def fill_missing_median(self):
        """
        Fill numeric missing values with column median.
        """
        numeric_cols = self.df.select_dtypes(include="number").columns

        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(
                self.df[col].median()
            )

        return self.df

    def fill_missing_mode(self):
        """
        Fill missing values with mode.
        """

        for col in self.df.columns:
            self.df[col] = self.df[col].fillna(
                self.df[col].mode()[0]
            )

        return self.df

    def drop_missing(self):
        """
        Remove rows containing missing values.
        """

        self.df = self.df.dropna()

        return self.df

    # -------------------------
    # Duplicate Handling
    # -------------------------

    def remove_duplicates(self):
        """
        Remove duplicate rows.
        """

        self.df = self.df.drop_duplicates()

        return self.df

    # -------------------------
    # Column Operations
    # -------------------------

    def drop_columns(self, columns):
        """
        Drop selected columns.

        Parameters
        ----------
        columns : list
        """

        self.df = self.df.drop(columns=columns)

        return self.df

    # -------------------------
    # Encoding
    # -------------------------

    def encode_categorical(self):
        """
        Label encode all categorical columns.
        """

        encoder = LabelEncoder()

        categorical = self.df.select_dtypes(
            include="object"
        ).columns

        for col in categorical:
            self.df[col] = encoder.fit_transform(
                self.df[col].astype(str)
            )

        return self.df

    # -------------------------
    # Scaling
    # -------------------------

    def standardize_numeric(self):
        """
        Standard scaling.
        """

        scaler = StandardScaler()

        numeric = self.df.select_dtypes(
            include="number"
        ).columns

        self.df[numeric] = scaler.fit_transform(
            self.df[numeric]
        )

        return self.df

    def minmax_scale(self):
        """
        Min-Max scaling.
        """

        scaler = MinMaxScaler()

        numeric = self.df.select_dtypes(
            include="number"
        ).columns

        self.df[numeric] = scaler.fit_transform(
            self.df[numeric]
        )

        return self.df

    # -------------------------
    # Export
    # -------------------------

    def get_clean_data(self):
        """
        Return cleaned dataframe.
        """

        return self.df