from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Route the home page to this function
@app.route('/')
def hello_world():
    """Returns a simple greeting message."""
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run() starts the local server
    app.run(host='0.0.0.0', port=5000)