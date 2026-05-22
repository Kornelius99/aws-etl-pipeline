import pandas as pd
from pathlib import Path


RAW_DATA_PATH = Path("data/raw/sales_data.csv")
PROCESSED_DATA_PATH = Path("data/processed/clean_sales_data.csv")


def transform_sales_data():
    """
    Clean and transform raw sales data.
    """

    df = pd.read_csv(RAW_DATA_PATH)

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert order date
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]

    # Add calculated field
    df["load_timestamp"] = pd.Timestamp.now()

    # Create processed directory if missing
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save processed data
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("Transformation completed successfully")
    print(f"Processed records: {len(df)}")

    return df


if __name__ == "__main__":
    transformed_df = transform_sales_data()

    print(transformed_df.head())