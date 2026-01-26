from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Route the home page to this function
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run() starts the local server
    app.run(host='0.0.0.0', port=5000)