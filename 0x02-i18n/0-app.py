#!/usr/bin/env python3
"""this module creates a Flask app"""
from flask import Flask, render_template
from typing import Any
app = Flask(__name__)

@app.route('/')
def index() -> Any:
    """
    Renders the index template.

    Returns:
        The rendered index template.
    """
    return render_template('0-index.html')
