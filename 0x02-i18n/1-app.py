#!/usr/bin/env python3
"""basic babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    '''default route'''
    return render_template("1-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
