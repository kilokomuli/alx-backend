#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    """default route"""
    return render_template("0-index.html")