#!/usr/bin/python3
from flask import Flask, escape, render_template
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


@app.route('/number/<int:n>')
def display_int(n):
    """ print n is a number if int"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def get_num(n):
    """ return HTML page with n in h1 if n is int """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def get_num_even_odd(n):
    """ return HTML page with n and if its even or odd in h1
    if n is int """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
