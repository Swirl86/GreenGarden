# Rename to main.py, put index.html in folder named templates
# Run command python main.py

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, json, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
