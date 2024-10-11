import sqlite3
import datetime

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL, "
           "balance "
           "INT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history(time TIMESTAMP NOT NULL, "
           "account INTEGER NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, "
           "account))")
db.execute("CREATE VIEW IF NOT EXISTS localtime AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, "
           "'localtime') AS localtime, account, amount FROM history ORDER BY history.time")


# def adapt_datetime_iso(val):
#     """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
#     return val.isoformat()
# 
#
# sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)


class Account:

    @staticmethod
    def get_time():
        return datetime.datetime.now(datetime.UTC)

    def __init__(self, name: str, starting_balance: int = 0, ):
        # cursor = db.cursor()
        cursor = db.execute("SELECT name, balance FROM accounts WHERE name "
                            "= ?", (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row
            print(f"Account {self.name} retrieve from the database.")
        else:
            self.name = name
            self._balance = starting_balance
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (self.name,
                                                                  self._balance))
            cursor.connection.commit()
            print(f"Account {self.name} created successfully.")
        self.show_balance()

    def record_updates(self, amount):
        new_balance = self._balance + amount
        db.execute("UPDATE accounts SET balance = ? WHERE name = ?",
                   (new_balance, self.name))
        deposit_time = Account.get_time()
        db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time,
                                                           self.name, amount))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0:
            self.record_updates(amount)  # Recording the depositing transaction into the database.
            print(f"{amount / 100:.2f} deposited.")
        else:
            print("Invalid deposit amount.")
        return self._balance

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self.record_updates(-amount)  # recording the withdrawing transaction into the database
            print(f"Account {self.name} withdraw {amount:.2f} ")
            return self._balance
        else:
            print("Withdraw amount mustn't be zero or above balance.")
            return 0.0

    def show_balance(self) -> None:
        print(f"Account {self.name} has {self._balance / 100:.2f} balance.")


if __name__ == "__main__":
    pine = Account("Pine")
    pine.deposit(1000)
    pine.deposit(10)
    pine.withdraw(50)
    pine.show_balance()

    yvan = Account("Yvan", 5000)
    jane = Account("Jane", 35400)
    doe = Account("Doe", 35000)
    james = Account('James')
    terry = Account('TerryG')
    db.close()
