import sqlite3
import pickle

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM history"):
    print(row)

db.close()
