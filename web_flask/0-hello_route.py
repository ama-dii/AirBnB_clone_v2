#!/usr/bin/python3
"""
Import flask
"""
from flask import Flask
app = Flask(__name__)

# Define the rout for the roo URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    # start flask development server
    # listen on all available network interface (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
