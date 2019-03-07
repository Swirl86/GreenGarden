#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# https://stackoverflow.com/questions/10752055/cross-origin-requests-are-only-supported-for-http-error-when-loading-a-local
# http://flask.pocoo.org/docs/1.0/quickstart/#static-files
# Run command: python main.py


from flask import Flask, json, request
from flask import render_template
from flask import redirect, url_for
import time
from threading import Thread

app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.route("/")  # URL '/' to be handled by main() route handler
def home():
    # Waiter().start()  # Vänta 30min

    filedata = []
    with open('static/test.txt') as fp:  # NOTERA: uppdatera filvägen
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

    return render_template('index.html', sensor=filedata)


# class Waiter(Thread):
#     def run(self):
#         x = 0
#         while x <= 180:
#             time.sleep(10)
#             x += 1


if __name__ == "__main__":  # Script executed directly?
    # Launch built-in web server and run this Flask webapp
    app.run(use_reloader=True, debug=True)
