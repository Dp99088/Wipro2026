import requests

BASE_URL = "http://127.0.0.1:5000/api/patients"

# POST patient
response = requests.post(BASE_URL, json={
    "name": "Durga Prasad",
    "age": 23,
    "Gender": "Male",
    "disease": "Fever",
    "doctor": "Dr. Smith"
})
print("POST:", response.status_code, response.json())

# GET all patients
response = requests.get(BASE_URL)
print("GET:", response.json())

# Negative test
response = requests.post(BASE_URL, json={})
print("NEGATIVE:", response.status_code)
