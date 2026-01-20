class Vehicle:
    count = 0

    def __init__(self):
        Vehicle.count += 1

    def start(self):
        print("Vehicle is starting")


class Car1(Vehicle):
    def drive(self):
        print("Car1 is driving")

class Car2(Vehicle):
    def d(self):
        print("Car2 is driving")

v1 = Vehicle()
c1 = Car1()
c2 = Car2()

#v1.start()
c1.start()
c2.start()
c1.drive()
c2.d()

print("Total vehicles created: ", Vehicle.count)


