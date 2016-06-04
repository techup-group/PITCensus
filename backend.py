#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for, flash
import flask, jinja2
import sys, json, os
import html

# ---------------------------------------------------------------------------- #

#Flask Application
app = Flask("THHI Homeless PIT Survey", static_url_path = "")
app.secret_key = "roflmao"

# ---------------------------------------------------------------------------- #
# Routing (wiring)

#Root page, shows the main input form and initial data
@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", general_inputs=html.index_general_inputs)

#The route to POST to when a user fills out the data in index.html
@app.route('/submit', methods=['POST'])
def submit_form():
	pass

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port=5000)

