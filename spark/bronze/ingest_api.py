import requests
from save_raw_data import save_raw_data

API_URL = "https://fakestoreapi.com/products"

def fetch_products():
    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"API request failed: {response.status_code}")


if __name__ == "__main__":

    products = fetch_products()

    save_raw_data(products)

    print(f"Fetched {len(products)} products")