from abc import ABC, abstractmethod

class bank(ABC):
    @abstractmethod
    def Interest(self):
        pass
    @abstractmethod
    def loan(self):
        pass
class ABI(bank):
    def Interest(self):
        print("Interest is 5%")
    def loan(self):
        print("Loan is available")
s1=ABI()
s1.Interest()
s1.loan()