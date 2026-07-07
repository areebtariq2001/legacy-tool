class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            print "Insufficient funds"
        else:
            self.balance = self.balance - amount
            print "New balance:", self.balance

acc = Account(100)
acc.withdraw(30)
