import pytest
import os
import json

BASE_URL = "http://127.0.0.1:5006"

FILES = [
    "restaurants.json",
    "dishes.json",
    "users.json",
    "orders.json",
    "ratings.json"
]

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session", autouse=True)
def clean_files():
    """Reset JSON files before tests"""
    for file in FILES:
        with open(file, "w") as f:
            json.dump([], f)