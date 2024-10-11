import sqlite3

db = sqlite3.connect("test_database.sqlite")
new_email = 'newepdated@email.com'
phone = input("Enter phone: ")

update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)

cursor_update = db.cursor()
cursor_update.execute(update_sql, (new_email, phone))
print(f"{cursor_update.rowcount} row(s) updated.")

print(f"Are connections the same: {cursor_update.connection == db}")

cursor_update.connection.commit()
cursor_update.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

