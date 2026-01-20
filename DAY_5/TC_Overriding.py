class animal:
    def sound(self):
        print("Animal sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Meow")

obj =(dog(), cat())

for a in obj:
    a.sound()