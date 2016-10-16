#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for
import sys, json, os

# ---------------------------------------------------------------------------- #
# Flask Application
app = Flask(__name__, static_url_path = "")
app.secret_key = "roflmao"

# ---------------------------------------------------------------------------- #
# Routing (wiring)

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
