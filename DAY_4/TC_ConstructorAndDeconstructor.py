class Employee:
    def __init__(self, name):
        self.name = name
        print("Constructot is called")

    def display(self):
        print(f"My name is {self.name}")

    def __del__(self):
        print("Destructor is called")


e1 = Employee("Durga")
e1.display()
