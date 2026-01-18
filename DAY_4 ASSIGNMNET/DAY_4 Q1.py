class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display_details(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)

s1=student("Durga",1) 
s2=student("Balu",2)

s1.display_details()
s2.display_details()