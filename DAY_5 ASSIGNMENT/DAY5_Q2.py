class Calculator:
    def add(self, a, b):
        print("Calculator")
        return a + b


class AdvancedCalculator(Calculator):

    def add(self, a, b, c=0):
        print("AdvancedCalculator")
        return a + b + c

calc = Calculator()
adv_calc = AdvancedCalculator()

print(calc.add(10, 20))
print(adv_calc.add(10, 20))
print(adv_calc.add(10, 20, 30))
