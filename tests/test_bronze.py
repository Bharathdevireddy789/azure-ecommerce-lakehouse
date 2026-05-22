from spark.bronze.ingest_api import fetch_products


def test_fetch_products():

    products = fetch_products()

    assert products is not None
    assert len(products) > 0
