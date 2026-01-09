import sqlite3  # sqlite3 is Python’s built-in library for working with SQLite databases.

database_file = "library.db"  # this will create database in sqlite3


def open_connection():
    return sqlite3.connect(database_file)

def database_setup():
    conn = open_connection()
    cursor = conn.cursor() # Cursor is used to execute SQL commands

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS library_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            published_year INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_books(book_list):
    conn = open_connection()
    cursor = conn.cursor()

    for book in book_list:
        cursor.execute(
            """
            INSERT INTO library_books (title, author, published_year)
            VALUES (?, ?, ?)
            """,
            (book["title"], book["author"], book["year"])
        )

    conn.commit()
    conn.close()


def read_books():
    conn = open_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT title, author, published_year FROM library_books"
    )
    records = cursor.fetchall()

    conn.close()
    
    return records
