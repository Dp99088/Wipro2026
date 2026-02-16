import requests
import pytest

@pytest.mark.parametrize("payload, status", [
    ({"name": "Durga", "email": "durga1@gmail.com", "password": "1234"}, 201),
    ({"name": "", "email": "", "password": ""}, 400),
])

def test_user_registration(base_url, payload, status):

    r = requests.post(f"{base_url}/api/v1/users/register", json=payload)

    assert r.status_code == status