import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/sales_data.csv")


def load_sales_data(file_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load raw sales dataset.
    """

    df = pd.read_csv(file_path)

    print("Data loaded successfully")
    print(f"Total records: {len(df)}")

    return df


if __name__ == "__main__":
    sales_df = load_sales_data()

    print(sales_df.head())