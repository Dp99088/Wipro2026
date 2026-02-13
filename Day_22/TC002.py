from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["C1"]

# INSERT
data = {
    "name": "Durga Prasad",
    "dept": "IT",
    "salary": 30000
}

collection.insert_one(data)
print("Inserted")

# READ
print("\nAll Records:")
for record in collection.find():
    print(record)
