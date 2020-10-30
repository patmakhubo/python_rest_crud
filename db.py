import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, addr TEXT, city TEXT, pin TEXT)")

conn.close();