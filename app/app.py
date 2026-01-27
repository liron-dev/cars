import os
import psycopg2
from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'), # Default to 'db' (service name)
        database=os.environ.get('DB_NAME', 'cars_db'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASS', 'password')
    )
    return conn

# Temporary Database:
CARS_DATA = [
    {
        "name": "Porsche 911 GT3 RS",
        "hp": 518,
        "engine": "4.0L Flat-6",
        "description": "The pinnacle of 911 performance. Built for the track, but legal for the road.",
        "image": "images/porsche.jpeg",
        "tags": ["German", "Track-Tool", "Naturally Aspirated"]
    },
    {
        "name": "DeLorean DMC-12",
        "hp": 130,
        "engine": "2.85L V6",
        "description": "The stainless steel icon. Does not actually come with a Flux Capacitor unless you provide the plutonium.",
        "image": "images/delorean.jpeg",
        "tags": ["Movie Icon", "Stainless Steel", "Gull-wing"]
    }
]

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, hp, engine, description, image, tags FROM cars;')
    rows = cur.fetchall()
    cars = []
    for row in rows:
        cars.append({
            "name": row[0],
            "hp": row[1],
            "engine": row[2],
            "description": row[3],
            "image": row[4],
            "tags": row[5].split(",")
        })

    cur.close()
    conn.close()
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    # app.run() starts the local server
    app.run(host='0.0.0.0', port=5000)