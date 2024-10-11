import sqlite3

db = sqlite3.connect('test_database.sqlite')

name = input("Enter name to display details: ").capitalize()

display_cursor = db.cursor()
display_sql = "SELECT * FROM contacts WHERE name LIKE ?"
retrieved = display_cursor.execute(display_sql, (name,))

for obj in retrieved:
    print(obj)

display_cursor.close()
db.close()
