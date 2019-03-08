#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, json, request
from threading import Thread
import time


app = Flask(__name__)  # Construct an instance of Flask class for our webapp
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")  # URL '/' to be handled by main() route handler
def home():

    filedata = []

    f = open("static/test.txt")

    with open('static/test.txt') as fp:  # NOTERA: update filepath
        for line in fp:
            str = line
            dataarray = str.split(',')
            it = iter(dataarray)
            ID1 = it.next()
            ID2 = it.next()
            ID3 = it.next()
            ID4 = it.next()
            theData = {
                'Date': ID2,
                'Time': ID3,
                'Moisture': ID1,
                'Watered': ID4
            }
            filedata.append(theData)

    f.close()

    return render_template('index.html', sensor=filedata)


if __name__ == "__main__":  # Script executed directly?
    # Launch built-in web server and run this Flask webapp
    app.run(host='localhost', port=8080, debug=False,
            threaded=True, use_reloader=False)
