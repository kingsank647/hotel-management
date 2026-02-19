from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            room_type TEXT,
            num_rooms INTEGER,
            num_guests INTEGER,
            arrival_date DATE,
            departure_date DATE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/book', methods=['POST'])
def book_room():
    data = request.get_json()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bookings
        (name, email, room_type, num_rooms, num_guests, arrival_date, departure_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['name'],
        data['email'],
        data['room_type'],
        data['num_rooms'],
        data['num_guests'],
        data['arrival_date'],
        data['departure_date']
    ))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "Booking successful!"})

if __name__ == "__main__":
    init_db()
    app.run()
