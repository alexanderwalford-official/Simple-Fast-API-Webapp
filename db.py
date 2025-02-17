import sqlite3

def create_table():
    """
        Create a table in the database.
    """
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    conn.commit()
    conn.close()

def insert_into_table (type, values):
    """
        Insert a row into the table. Takes table name and values as input.
    """
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO (?) VALUES (?, ?, ?)", type, values)
    conn.commit()
    conn.close()