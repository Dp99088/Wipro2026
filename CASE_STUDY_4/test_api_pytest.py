import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

@pytest.mark.parametrize("patient", [
    {"name": "Vijay", "age": 22},
    {"name": "Ajay", "age": 20}
])
def test_add_patient(patient):
    r = requests.post(BASE_URL, json=patient)
    assert r.status_code == 201

def test_get_patients():
    r = requests.get(BASE_URL)
    assert r.status_code == 200

@pytest.mark.skip(reason="Under development")
def test_skip():
    pass

@pytest.mark.xfail
def test_fail():
    assert False
