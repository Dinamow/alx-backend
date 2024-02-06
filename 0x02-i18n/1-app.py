#!/usr/bin/env python3
"""this module creates a Flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> Any:
    """
    Renders the index template.

    Returns:
        The rendered index template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
