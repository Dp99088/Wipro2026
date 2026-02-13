import mysql.connector
host="127.0.0.1"
user="root"
password="Root@123"
database="employee"
port=3306


conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

query="SELECT * FROM employees"
cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)