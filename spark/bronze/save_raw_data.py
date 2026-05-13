import json
import os
from datetime import datetime

RAW_PATH = "data/raw/products"

def save_raw_data(data):

    os.makedirs(RAW_PATH, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"{RAW_PATH}/products_{timestamp}.json"

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Saved raw data to {file_path}")