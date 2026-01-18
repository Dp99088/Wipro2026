from abc import ABC, abstractmethod


class Shape(ABC):
    def display(self):
        print("Display method")

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        print("Area method implemented")


s1 = Rectangle()
s1.area()
s1.display()