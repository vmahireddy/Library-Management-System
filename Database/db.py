import sqlite3
conn = None
def connect():
    global conn
    if conn is None:
        conn = sqlite3.connect(r"C:\Users\Prashanth reddy.A\Desktop\library_project\Database\library.db")
        create_tables()
def create_tables():
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    year INTEGER,
                    status TEXT
                    )''')
    conn.commit()
def execute_query(query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
def fetch_query(query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()