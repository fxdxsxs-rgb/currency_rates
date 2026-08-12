import unittest

from validator import validate_data


class TestValidateData(unittest.TestCase):
    def test_valid_data(self):
        data = {
            "result": "success",
            "base_code": "USD",
            "conversion_rates": {
                "AMD": 366.4864,
                "EUR": 0.85,
            },
        }

        self.assertTrue(validate_data(data))

    def test_missing_required_field(self):
        data = {
            "result": "success",
            "conversion_rates": {
                "AMD": 366.4864,
                "EUR": 0.85,
            },
        }

        self.assertFalse(validate_data(data))

    def test_api_returned_error(self):
        data = {
            "result": "error",
            "base_code": "USD",
        }

        self.assertFalse(validate_data(data))

    def test_wrong_base_currency(self):
        data = {
            "result": "success",
            "base_code": "RUB",
            "conversion_rates": {
                "USD": 1.17,
            },
        }

        self.assertFalse(validate_data(data))

    def test_rates_is_not_dict(self):
        data = {
            "result": "success",
            "base_code": "USD",
            "conversion_rates": [],
        }

        self.assertFalse(validate_data(data))

    def test_rates_is_empty(self):
        data = {
            "result": "success",
            "base_code": "USD",
            "conversion_rates": {},
        }

        self.assertFalse(validate_data(data))


if __name__ == "__main__":
    unittest.main()