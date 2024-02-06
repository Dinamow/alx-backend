#!/usr/bin/env python3
"""this module creates a Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Any


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Gets the locale from the request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
