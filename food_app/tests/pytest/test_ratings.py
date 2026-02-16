import requests

def test_give_rating(base_url):

    payload = {
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent"
    }

    r = requests.post(f"{base_url}/api/v1/ratings", json=payload)

    assert r.status_code == 201
    assert r.json()["rating"] == 5