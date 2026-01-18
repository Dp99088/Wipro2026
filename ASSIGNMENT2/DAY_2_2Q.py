class salarydescriptor:
    def __get__(self, obj, owner):
        return obj.__dict__.get("salary")

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj.__dict__["salary"] = value


class Employee:
    salary = salarydescriptor()   # descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Durga", 20000)
emp2 = Employee("Balu", 30000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)




