import logging
import os

import requests
from dotenv import load_dotenv


load_dotenv()

logger = logging.getLogger(__name__)
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
REQUEST_TIMEOUT = 5


def fetch_rates():
    if not API_KEY:
        logger.error("EXCHANGE_RATE_API_KEY not found .env")
        return None

    try:
        response = requests.get(
            API_URL,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        logger.error("Error during request: %s", error)
        return None

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error("API get incorrect data")
        return None