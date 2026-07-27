"""
Data loading utilities for the Automated EDA Platform.
"""

from pathlib import Path
import pandas as pd


SUPPORTED_EXTENSIONS = {".csv", ".xlsx", ".xls"}


def load_dataset(file) -> pd.DataFrame:
    """
    Load a CSV or Excel dataset.

    Parameters
    ----------
    file : str | Path | UploadedFile
        Path to a dataset or Streamlit uploaded file.

    Returns
    -------
    pandas.DataFrame
    """

    # Streamlit uploaded file
    if hasattr(file, "name"):

        extension = Path(file.name).suffix.lower()

        if extension not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        if extension == ".csv":
            return pd.read_csv(file)

        return pd.read_excel(file)

    # Local file path
    file_path = Path(file)

    if not file_path.exists():
        raise FileNotFoundError(
            f"{file_path} does not exist."
        )

    extension = file_path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    if extension == ".csv":
        return pd.read_csv(file_path)

    return pd.read_excel(file_path)