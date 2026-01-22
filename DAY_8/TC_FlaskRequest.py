import requests

geturl ="http://127.0.0.1:5000/users"

response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())

posturl ="http://127.0.0.1:5000/users"

body1 = {
    "name": "Ajay",
}

r1 = requests.post(posturl,json=body1)
print("post status code", r1.status_code)
print(r1.json())

puturl ="http://127.0.0.1:5000/users/2"
body2 = {
    "name": "Balu",
}
r2 = requests.put(puturl,json=body2)
print("put status code", r2.status_code)
print(r2.json())

patch_url ="http://127.0.0.1:5000/users/2"
body3 = {
    "name": "Balu Updated",
}
r3 = requests.patch(patch_url,json=body3)
print("patch status code", r3.status_code)
print(r3.json())

delete_url ="http://127.0.0.1:5000/users/2"

r4 = requests.delete(delete_url)
print("delete status code", r4.status_code)
print(r4.json())

