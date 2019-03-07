# https://stackoverflow.com/questions/10752055/cross-origin-requests-are-only-supported-for-http-error-when-loading-a-local
# http://flask.pocoo.org/docs/1.0/quickstart/#static-files
# Run command: python main.py

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, json, request
from flask import render_template
from flask import redirect, url_for
import datetime

app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.route("/")  # URL '/' to be handled by main() route handler
def home():
    now = datetime.datetime.now()
    dateString = now.strftime("%Y-%m-%d")
    timeString = now.strftime("%H:%M")

    dummyData = [
        {
            'Date': dateString,
            'Time': timeString,
            'Humidity': 530,
            'Watered': '09:50'
        },
        {
            'Date': dateString,
            'Time': timeString,
            'Humidity': 630,
            'Watered': '00:50'
        },
        {
            'Date': dateString,
            'Time': timeString,
            'Humidity': 430,
            'Watered': '09:50'
        }
    ]
    return render_template('index.html', sensor=dummyData)

# Test för senare http://mattrichardson.com/Raspberry-Pi-Flask/
# https://www.fontenay-ronan.fr/web-interface-for-raspberrys-sensors-gpio/
# https://electronicshobbyists.com/how-to-set-up-a-raspberry-pi-web-server/
# https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer-part-2/miniature-web-applications-in-python-with-flask
@app.route("/readPin/<pin>")
def readPin(pin):
    try:
        GPIO.setup(int(pin), GPIO.IN)
        if GPIO.input(int(pin)) == True:
            response = "Pin number " + pin + " is high!"
        else:
            response = "Pin number " + pin + " is low!"
    except:
        response = "There was an error reading pin " + pin + "."

    templateData = {
        'title': 'Status of Pin' + pin,
        'response': response
    }

    return render_template('pin.html', **templateData)


if __name__ == "__main__":  # Script executed directly?
    # Launch built-in web server and run this Flask webapp
    app.run(use_reloader=True, debug=True)
