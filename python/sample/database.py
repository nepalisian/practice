
import sqlite3

connection = sqlite3.connect("database.sqlite")

c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    age integer NOT NULL )
''')

c.execute('''INSERT INTO users (
    name, age
    )
    VALUES (
    'Ram', 24 ) 
''')

connection.commit()

connection.close()