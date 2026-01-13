class MyError(Exception):
    pass

class invalidage(Exception):
    pass

try:
    age=int(input("Enter your age: "))
    if age<18:
        raise invalidage("Age must be 18 or above")
    else:
        print("Eligible to Vote")
except invalidage as e:
    print("Error:",e)