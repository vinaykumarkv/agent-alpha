import sqlite3

DB_PATH = "db/audit.db"


def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("db/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


if __name__ == "__main__":
    initialize_db()