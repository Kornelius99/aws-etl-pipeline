from ingestion.load_data import load_sales_data
from transformation.clean_transform import transform_sales_data
from validation.validate_data import validate_sales_data
from loading.load_processed_data import load_processed_data


def run_pipeline():
    print("Starting AWS ETL Pipeline")

    load_sales_data()
    transform_sales_data()
    validate_sales_data()
    load_processed_data()

    print("AWS ETL Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
