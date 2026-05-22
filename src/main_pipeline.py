from ingestion.load_data import load_sales_data
from transformation.clean_transform import transform_sales_data
from validation.validate_data import validate_sales_data
from loading.load_processed_data import load_processed_data
from utils.logger import get_logger


logger = get_logger()


def run_pipeline():
    logger.info("Starting AWS ETL Pipeline")

    load_sales_data()
    logger.info("Ingestion completed")

    transform_sales_data()
    logger.info("Transformation completed")

    validate_sales_data()
    logger.info("Validation completed")

    load_processed_data()
    logger.info("Loading completed")

    logger.info("AWS ETL Pipeline completed successfully")

    print("Pipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()
