from kafka import KafkaProducer
import json
from ingest_api import fetch_products

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC_NAME = "orders"

def send_products():

    products = fetch_products()

    for product in products:

        producer.send(TOPIC_NAME, value=product)

        print(f"Sent product ID: {product['id']}")

    producer.flush()


if __name__ == "__main__":
    send_products()