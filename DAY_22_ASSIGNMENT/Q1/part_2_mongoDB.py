from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

employee = {
    "name": "kavya",
    "department": "HR",
    "salary": 56000
}

collection.insert_one(employee)
print("Employee Inserted Successfully")

print("Employees in IT Department")
query = {"department": "IT"}
records = collection.find(query)
for emp in records:
    print(emp)

collection.update_one(
    {"name": "raju"},
    {"$set":{"salary":55000}},
)

print("Salary Updated Successfully")
client.close()