class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created:", self.account_number)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)

    def __del__(self):
        print("Account deleted:", self.account_number)

account = BankAccount(2345678, 10000)

account.deposit(2000)
account.withdraw(3000)
account.withdraw(7000)   