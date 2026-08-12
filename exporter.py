import json
import logging
from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
logger = logging.getLogger(__name__)


def save_json(data):
    DATA_DIR.mkdir(exist_ok=True)

    with open(
        DATA_DIR / "rates.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )
    logger.info("JSON saved")


def create_dataframe(data):
    return pd.DataFrame(
        [
            {
                "currency": currency,
                "rate_to_usd": rate,
            }
            for currency, rate in data["conversion_rates"].items()
        ]
    )


def save_csv(dataframe):
    dataframe.to_csv(
        DATA_DIR / "rates.csv",
        index=False,
        encoding="utf-8-sig",
    )
    logger.info("CSV saved")


def save_xlsx(dataframe):
    dataframe.to_excel(
        DATA_DIR / "rates.xlsx",
        index=False,
    )
    logger.info('XLSX saved')


def export_data(data):
    save_json(data)
    dataframe = create_dataframe(data)
    save_csv(dataframe)
    save_xlsx(dataframe)