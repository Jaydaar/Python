import sqlite3

db =sqlite3.connect("accounts.sqlite")
db.execute("create table if not exists accounts (name text primary key not null, balance integer not null)")
db.execute("create table if not exists transactions (time timestamp not null," \
" account text not null, amount integer not null, primary key (time, account))")

class Account(object):

    def __init__(self, name: str, opening_balance: int = 0.0):
        cursor = db.execute("select name, balance from accounts where (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("insert into accounts values(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end="")
        self.show_balance()

    def deposit(self, amount: int) -> float:
        """ Takes a float argument for and amount and returns a float for the
        balance after the amount was deposited."""
        if amount > 0.0:
            self._balance += amount
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print(
                "The amount must e greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("Terry")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)

    db.close()
