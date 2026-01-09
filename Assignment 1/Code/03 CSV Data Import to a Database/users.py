import csv
import sqlite3

db = "users.db"
csv_file = "users.csv"

def create_database():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL)")
    conn.commit()
    conn.close()


def load_csv_into_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    with open(csv_file) as f:
        reader = csv.reader(f)

        for r in reader:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (r[0], r[1]))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    load_csv_into_db()
