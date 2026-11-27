# Parent Class
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Balance: KSh", self.balance)


# Child Class
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculateInterest(self):
        return (self.balance * self.interest_rate) / 100


# Main Program
account = SavingsAccount("ACC1001", 50000, 5)

account.displayAccount()
print("Interest Rate:", account.interest_rate, "%")
print("Calculated Interest: KSh", account.calculateInterest())

