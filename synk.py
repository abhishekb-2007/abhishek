import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()

username = input("Enter username: ")

# BAD: directly inserting user input into SQL
query = f"SELECT * FROM users WHERE username = '{username}'"
print("Running query:", query)

cur.execute(query)
print(cur.fetchall())
