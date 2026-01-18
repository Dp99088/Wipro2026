from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        print(self.name, "salary is 50000")


m1 = Manager("Durga")
m1.salary()