#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
import flask, jinja2
import sys, json, os
import html

# ---------------------------------------------------------------------------- #
# connect database
conn = sqlite3.connect('database.db')

# create cursor
c = conn.cursor()

# create main table
try: c.execute('''CREATE TABLE entries
				(volunteer, sleep_location, sleep_location_detail, first_name, last_name, ssn, dob, age)''')
except: pass

# ---------------------------------------------------------------------------- #
# Flask Application
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
	print request.form
	return redirect('/')

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port=5000)

