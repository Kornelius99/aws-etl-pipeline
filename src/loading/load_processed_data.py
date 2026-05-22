import pandas as pd
from pathlib import Path


PROCESSED_DATA_PATH = Path("data/processed/clean_sales_data.csv")
FINAL_OUTPUT_PATH = Path("data/processed/final_sales_dataset.csv")


def load_processed_data():
    df = pd.read_csv(PROCESSED_DATA_PATH)

    FINAL_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(FINAL_OUTPUT_PATH, index=False)

    print("Processed data loaded successfully")
    print(f"Final output path: {FINAL_OUTPUT_PATH}")
    print(f"Loaded records: {len(df)}")

    return df


if __name__ == "__main__":
    load_processed_data()
