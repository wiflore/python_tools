class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount

    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


#Inheritance

class Checking(Account):

    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance=self.balance-amount


checking = Checking("balance.txt")
checking.transfer(100)


account = Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()
