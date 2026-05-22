import pandas as pd
from pathlib import Path


PROCESSED_DATA_PATH = Path("data/processed/clean_sales_data.csv")


REQUIRED_COLUMNS = [
    "order_id",
    "customer_id",
    "order_date",
    "region",
    "product_category",
    "product_name",
    "quantity",
    "unit_price",
    "total_amount",
    "payment_method",
    "load_timestamp"
]


def validate_sales_data():
    df = pd.read_csv(PROCESSED_DATA_PATH)

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df["order_id"].isnull().any():
        raise ValueError("Validation failed: order_id contains null values")

    if df["total_amount"].isnull().any():
        raise ValueError("Validation failed: total_amount contains null values")

    if (df["total_amount"] <= 0).any():
        raise ValueError("Validation failed: total_amount contains invalid values")

    print("Data validation completed successfully")
    print(f"Validated records: {len(df)}")

    return True


if __name__ == "__main__":
    validate_sales_data()
