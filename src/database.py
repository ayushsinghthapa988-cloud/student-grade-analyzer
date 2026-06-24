import sqlite3

def connect_db():
    conn = sqlite3.connect("student_database.db")
    return conn
