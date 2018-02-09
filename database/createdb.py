import sqlite3
db = sqlite3.connect("contacts.sqlite")
db.execute("create table if not exists contacts (name text, phone integer, email text)")
db.execute("insert into contacts(name, phone, email) values('Kevin', 3320629, 'kevin@email.com')" )
db.execute("insert into contacts values('tim', 1234, 'tim@email.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")
for row in cursor:
    print(row)

cursor.close()
db.close()