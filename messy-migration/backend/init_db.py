import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Drop existing users table
cursor.execute("DROP TABLE IF EXISTS users")

# Create new users table with password
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    gender TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert sample users
users = [
    ("Alice", "alice@example.com", "female", "alice123"),
    ("Bob", "bob@example.com", "male", "bob123"),
    ("Charlie", "charlie@example.com", "male", "charlie123"),
    ("Diana", "diana@example.com", "female", "diana123")
]

cursor.executemany("INSERT INTO users (name, email, gender, password) VALUES (?, ?, ?, ?)", users)
conn.commit()
conn.close()
