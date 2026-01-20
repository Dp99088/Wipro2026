class Parent:
    def parent1(self):
        print("Parent 1")

class Child1(Parent):
    def c1(self):
        print("Child 1")

class Child2(Parent):
    def c2(self):
        print("Child 2")

c1 = Child1()
c1.c1()
c1.parent1()

c2 = Child2()
c2.parent1()
c2.c2()
