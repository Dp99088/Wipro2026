import requests

geturl ="https://api.restful-api.dev/objects"

response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())

posturl ="https://api.restful-api.dev/objects"

body1 = {
    "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1 = requests.post(posturl, json=body1)
print("post status code", r1.status_code)
print(r1.json())

puturl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4010c432e56"

body2 = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r2 = requests.put(puturl, json=body2)
print("put status code", r2.status_code)
print(r2.json())

patchurl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4010c432e56"

body3 = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

r3 = requests.patch(patchurl, json=body3)
print("patch status code", r3.status_code)
print(r3.json())

deleteurl = "https://api.restful-api.dev/objects/ff8081819782e69e019be4010c432e56"

r4 = requests.delete(deleteurl)
print("delete status code", r4.status_code)
print(r4.json())