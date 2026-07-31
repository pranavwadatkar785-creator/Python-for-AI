import sqlite3

conn = sqlite3.connect(r"C:\Users\Pranav Wadatkar\Desktop\Python\python-for-ai\practice week4\example.db")

cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")