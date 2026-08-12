import logging

from api import fetch_rates
from exporter import export_data
from logger import setup_logging
from validator import validate_data

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    logger.info("script currency_rates start")

    data = fetch_rates()

    if data is None:
        return

    if not validate_data(data):
        return

    export_data(data)

    logging.info("Script currency_rates success")


if __name__ == "__main__":
    main()