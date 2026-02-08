import requests

geturl ="http://127.0.0.1:5001/api/movies"

response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())

posturl ="http://127.0.0.1:5001/api/movies"

body1 = {
    "id": 103,
    "movie_name": "Avatar",
    "language": "English",
    "duration": "2h 28m",
    "price": 150
}

r1 = requests.post(posturl,json=body1)
print("post status code", r1.status_code)
print(r1.json())

puturl ="http://127.0.0.1:5001/api/movies/103"
body2 = {
    "language": "Hindi",
    "price": 350
}
r2 = requests.put(puturl,json=body2)
print("put status code", r2.status_code)
print(r2.json())

delete_url ="http://127.0.0.1:5001/api/movies/102"

r4 = requests.delete(delete_url)
print("delete status code", r4.status_code)
print(r4.json())



booking_url = "http://127.0.0.1:5001/api/bookings"

booking_body = {
    "movie_id": 102,
    "seats": 7
}

r5 = requests.post(booking_url, json=booking_body)

print("booking status code", r5.status_code)
print(r5.json())