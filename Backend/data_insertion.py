import sqlite3
from process_sms import parse_sms_data

DB_NAME = "../Data/sms_transactions.db"

def insert_into_db(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for entry in data:
        cursor.execute('''
        INSERT INTO transactions (category, amount, timestamp, message) 
        VALUES (?, ?, ?, ?)
        ''', entry)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    sms_data = parse_sms_data("../Data/sms_data.xml")
    insert_into_db(sms_data)
    print("Data inserted successfully!")
