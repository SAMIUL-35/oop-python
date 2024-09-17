class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Fokira. You can withdraw up to {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'Fajil, You can withdraw down to {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here, your money is: {self.balance}')

DBBL = bank(15000)
DBBL.get_balance()
DBBL.withdraw(5)