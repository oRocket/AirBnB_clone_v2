#!/usr/bin/python3
"""
A script that starts a Flask web application
"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display a message when / is called """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display hbnb message when /hbnb is called """
    return 'HBNB'

if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=5000)
