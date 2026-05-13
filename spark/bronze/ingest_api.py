import requests

from save_raw_data import save_raw_data
from utils import setup_logger

API_URL = "https://fakestoreapi.com/products"

logger = setup_logger()


def fetch_products():

    logger.info("Fetching product data from FakeStore API")

    response = requests.get(API_URL)

    if response.status_code == 200:

        logger.info("Successfully fetched product data")

        return response.json()

    logger.error(f"API request failed: {response.status_code}")

    raise Exception(f"API request failed: {response.status_code}")


if __name__ == "__main__":

    products = fetch_products()

    save_raw_data(products)

    logger.info(f"Saved {len(products)} products successfully")