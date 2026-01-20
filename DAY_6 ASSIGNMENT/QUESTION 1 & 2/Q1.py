import re

emp_id = "EMP123"
pattern = r"EMP\d{3}"

result = re.match(pattern,emp_id)

if result:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")

#Q2
email = "Employee email is emp123@gmail.com"
result1 = re.search(r"\w+@\w+\.\w+", email)
print("Email found", result1.group())

#Q3

text1 = "cat bat rat"
print(re.findall(r".at", text1))

text2 = "ab abb abbb a"
print(re.findall(r"ab*", text2))

text3 = "ab abb abbb a"
print(re.findall(r"ab+", text3))

text4 = "color colour"
print(re.findall(r"colou?r", text4))


text5 = "Order numbers: 45, 789, 12"
print(re.findall(r"\d+", text5))

text6 = "user_1 user-2 user3"
print(re.findall(r"\w+", text6))

text7 = "Hello   World\tPython"
print(re.findall(r"\s+", text7))

#Q4

tx = "Name: EMP123 Age: 23 Email: emp123@gmail.com"

pattern = r"Name:\s(\w+)\sAge:\s(\d+)\sEmail:\s(\w+@\w+\.\w+)"

match = re.search(pattern, tx)

if match:
    print("Full Match :", match.group(0))
    print("Name       :", match.group(1))
    print("Age        :", match.group(2))
    print("Email      :", match.group(3))