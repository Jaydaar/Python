import sqlite3

db =sqlite3.connect("accounts.sqlite")
db.execute("create table if not exists accounts (name text primary key not null, balance integer not null")
db.execute("create table if not exits transactions (time timestamp not null,"
" account text not null, amount integer not null, primary key (time, account))")


from decimal import *

class Account(object):
    _qb = Decimal("0.0000")

    def __init__(self, name:str, opening_balance:float=0.0):
        self.name = name
        self._balance = Decimal(opening_balance).quantize(Account._qb)
        print("Account create for {}.".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount:float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            self._balance = self._balance + decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._balance

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            self._balance = self._balance - decimal_amount
            print("{} withdrawn".format(decimal_amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return Account._qb

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))


if __name__ == "__main__":
    kevin = Account("Kevin")
    kevin.deposit(10.10)
    kevin.deposit(0.10)
    kevin.deposit(0.10)
    kevin.withdraw(0.30)
    kevin.withdraw(0.0)
    kevin.show_balance()
