"""
Data loading utilities for the Automated EDA Platform.
"""

from pathlib import Path
import pandas as pd


SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}


def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """
    Load a CSV or Excel dataset.

    Parameters
    ----------
    file_path : str | Path
        Path to the dataset.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    extension = file_path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}. "
            f"Supported formats: {SUPPORTED_EXTENSIONS}"
        )

    if extension == ".csv":
        return pd.read_csv(file_path)

    return pd.read_excel(file_path)