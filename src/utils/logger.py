import logging
from pathlib import Path


LOG_PATH = Path("logs")

LOG_PATH.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():
    return logging.getLogger()
