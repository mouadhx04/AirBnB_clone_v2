#!/usr/bin/python3
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ print Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ print HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def grab_text(text):
    """ print HBNB"""
    return "C %s" % escape(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def grab_python_text(text):
    """ print HBNB"""
    return "Python %s" % escape(text.replace("_", " "))


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
