import logging


REQUIRED_FIELDS = {
    "result",
    "base_code",
    "conversion_rates",
}
logger = logging.getLogger(__name__)


def validate_data(data):
    if not isinstance(data, dict):
        logger.error("API answer must be a dict")
        return False

    if not REQUIRED_FIELDS.issubset(data):
        logger.error("Missing required fields")
        return False

    if data.get("result") != "success":
        logger.error("API request failed, not success status")
        return False

    if data.get("base_code") != "USD":
        logger.error("Got incorrect base_code")
        return False

    rates = data.get("conversion_rates")
    if not isinstance(rates, dict) or not rates:
        logger.error("conversion_rates is missing, not a dict, or empty")
        return False

    return True