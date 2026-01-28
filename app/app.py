import os
import psycopg2
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

# Create the Flask application instance
app = Flask(__name__)
# Export metrics to prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.3')

# Connect to DB
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'), # Default to 'db' (service name)
        database=os.environ.get('DB_NAME', 'cars_db'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASS', 'password')
    )
    return conn

# Pull data from DB
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
