import sqlite3

db = sqlite3.connect('test_database.sqlite')

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, "
           "email TEXT)")
db.execute("INSERT INTO contacts VALUES ('Pine', 1234, 'pine@mail.com')")
db.execute("INSERT INTO contacts VALUES ('Yvan', 1224, 'yvan@mail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

    print("-" * 20)

cursor.close()
db.commit()
db.close()
