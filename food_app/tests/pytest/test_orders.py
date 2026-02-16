import requests

def test_place_order(base_url):

    payload = {
        "user_id": 1,
        "restaurant_id": 1,
        "dishes": [1]
    }

    r = requests.post(f"{base_url}/api/v1/orders", json=payload)

    assert r.status_code == 201
    assert r.json()["status"] == "Placed"