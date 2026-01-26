from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

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

# Route the home page to this function
@app.route('/')
def index():
    return render_template('index.html', cars=CARS_DATA)

if __name__ == '__main__':
    # app.run() starts the local server
    app.run(host='0.0.0.0', port=5000)