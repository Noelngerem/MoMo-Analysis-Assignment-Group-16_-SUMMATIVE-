from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

DB_NAME = "../Data/sms_transactions.db"

@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    conn.close()
    
    transactions = [{"id": row[0], "category": row[1], "amount": row[2], "timestamp": row[3], "message": row[4]} for row in data]
    return jsonify(transactions)

if __name__ == "__main__":
    app.run(debug=True)
