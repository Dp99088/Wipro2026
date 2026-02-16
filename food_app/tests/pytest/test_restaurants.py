import requests
from jsonschema import validate

restaurant_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "category": {"type": "string"},
        "location": {"type": "string"},
        "images": {"type": "string"},
        "contact": {"type": "number"},
        "approved": {"type": "boolean"},
        "active": {"type": "boolean"}
    },
    "required": ["id", "name", "category", "location"]
}


def test_register_restaurant(base_url):

    payload = {
        "name": "Food Hub",
        "category": "Veg",
        "location": "Hyderabad",
        "images": "image.png",
        "contact": 9876543210
    }

    r = requests.post(f"{base_url}/api/v1/restaurants", json=payload)

    assert r.status_code == 201

    data = r.json()

    assert data["name"] == "Food Hub"

    validate(instance=data, schema=restaurant_schema)


def test_list_restaurants(base_url):

    r = requests.get(f"{base_url}/api/v1/restaurants")

    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_view_restaurant_not_found(base_url):

    r = requests.get(f"{base_url}/api/v1/restaurants/999")

    assert r.status_code == 404