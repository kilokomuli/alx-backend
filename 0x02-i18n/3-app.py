#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """default route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)