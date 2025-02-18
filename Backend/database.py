import sqlite3

DB_NAME = "../Data/sms_transactions.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount INTEGER,
        timestamp TEXT,
        message TEXT
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
