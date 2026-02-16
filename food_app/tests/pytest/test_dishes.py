import requests
from jsonschema import validate

dish_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "price": {"type": "number"},
        "enabled": {"type": "boolean"}
    },
    "required": ["id", "name"]
}


def test_add_dish(base_url):

    payload = {
        "name": "Paneer Curry",
        "type": "Main Course",
        "price": 250,
        "available_time": "10AM - 10PM",
        "image": "paneer.png"
    }

    r = requests.post(f"{base_url}/api/v1/restaurants/1/dishes", json=payload)

    assert r.status_code == 201

    validate(instance=r.json(), schema=dish_schema)


def test_update_dish(base_url):

    r = requests.put(f"{base_url}/api/v1/dishes/1", json={"price": 300})

    assert r.status_code == 200
    assert r.json()["price"] == 300