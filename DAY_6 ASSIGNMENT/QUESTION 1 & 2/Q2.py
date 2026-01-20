import re

password = "Admin@123"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$'

if re.search(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

#Q2
text = "Python"
pattern1 = "python"

result = re.search(pattern1, text, re.IGNORECASE)
print("Matched")

#Q3

text1 ="Hello\nPython"
pattern2 = r"^Python"

match = re.search(pattern2, text1, re.MULTILINE)
print(match.group())

text2 = "Hello\nWorld"
pattern3 = r"Hello.*World"
match = re.search(pattern3, text2, re.DOTALL)
print(match.group())