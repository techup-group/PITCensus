#!/usr/bin/env python
from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
import flask, jinja2
import sys, json, os
import html

# ---------------------------------------------------------------------------- #
# connect database
conn = sqlite3.connect('database.db', check_same_thread=False)

# create cursor
c = conn.cursor()

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

	# turn page's form data into a list
	unsorted_list = []
	for item in request.form.iterlists():
		unsorted_list.append(item)

	# create first part of sqlite execute string
	insert_str = "INSERT INTO entries VALUES ("

	print "\nUNSORTED form data: " + str(unsorted_list)
	print "\nSORTED form data: " + str(sorted(unsorted_list))

	# populate string with data from page forms
	for field in sorted(unsorted_list):
		insert_str += '"' + str(field[1]) + '",'

	# replace last , with ) to close statement
	insert_str = insert_str[:-1] + ')'

	print "\nsqlite INSERT string: " + insert_str + "\n"

	# UNCOMMENT
	# execute insert string
	# c.execute(insert_str)
	
	# save and exit database connection
	conn.commit()

	return redirect('/')

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port=5000)
    conn.close()

