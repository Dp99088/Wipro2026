import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Root@123",
    database="company_db",
    port=3306
)
cursor=conn.cursor()


print("Employees with Salary > 50,000:")

query1 = "SELECT * FROM employees WHERE salary > 50000"
cursor.execute(query1)

records = cursor.fetchall()

for row in records:
    print(row)

print("Inserting New Employee")

query2 = """
INSERT INTO employees (id, name, department, salary)
VALUES (%s, %s, %s, %s)
"""

values = (8, "pramodh", "IT", 52000)

cursor.execute(query2, values)
conn.commit()

print("Employee Inserted Successfully")

print("Updating Salary")

query3 = """
UPDATE employees
SET salary = salary * 1.10
WHERE name = %s
"""

cursor.execute(query3, ("raju",))
conn.commit()

print("Salary Updated Successfully")

cursor.close()
conn.close()

print("All Operations Completed Successfully")