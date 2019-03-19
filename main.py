#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, json, request
from threading import Thread
import time


app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.route("/")  # URL '/' to be handled by main() route handler
def home():

    count = 0
    getDataRow = []
    filedata = []

    # Get the data from the file
    with open('../data.txt', 'r') as fp:  # Note: update filepath
        for i in fp:
            str = i

            dataarray = str[str.index(': ') + 1:].split("\n")
            getDataRow.append(dataarray)
            if count == 3:
                ID1 = getDataRow[0]
                ID1 = ''.join(ID1)  # Remove brackets
                ID2 = getDataRow[1]
                ID2 = ''.join(ID2)
                ID3 = getDataRow[2]
                ID3 = ''.join(ID3)
                ID4 = getDataRow[3]
                ID4 = ''.join(ID4)
                theData = {
                    # Assign right value to column
                    'Date': ID2,
                    'Time': ID3,
                    'Moisture': ID1,
                    'Watered': ID4
                }
                filedata.append(theData)  # Append a complete data row
                count = 0
                getDataRow = []  # Reset to empty
            else:
                count += 1
    fp.close()

    return render_template('index.html', sensor=filedata)


if __name__ == "__main__":
    # Launch built-in web server and run this Flask webapp
    app.run(host='localhost', port=8080, debug=False,
            threaded=True, use_reloader=False)
