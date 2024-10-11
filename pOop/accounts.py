import datetime


class Account:

    @staticmethod
    def _transaction_recorder():
        date = datetime.datetime.now(datetime.UTC)
        return date

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        print(f"{self._name}'s account created successful!")
        self._transaction_history = [(Account._transaction_recorder(), self.__balance)]

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_history.append(
                (Account._transaction_recorder(), amount))
        else:
            print('Invalid amount!')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance()
            self._transaction_history.append((Account._transaction_recorder(),
                                              -amount))
        else:
            print('Invalid amount! or Not enough funds!')

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def show_transaction(self):
        for date, amount in self._transaction_history:
            if amount >= 0:
                print(f"\t{amount} Deposited on {date} localtime: "
                      f"{date.astimezone()}")
            else:
                print(f"\t{-amount} Withdrawn on {date} localtime: "
                      f"{date.astimezone()}")


pine = Account('Pine', 0)
pine.show_balance()
pine.deposit(200)
pine.withdraw(150)
# pine.withdraw(300)
pine.show_transaction()
pine.show_balance()

print()
bestie = Account('Bestie', 400)
bestie.show_balance()
bestie.deposit(2500)
bestie.withdraw(700)
# pine.withdraw(300)
bestie.show_transaction()
bestie.show_balance()
