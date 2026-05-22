import os


def test_gold_directory_exists():

    assert os.path.exists("data/processed/gold")
