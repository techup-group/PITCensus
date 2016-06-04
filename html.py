#!/usr/bin/env python
# Items to fill in HTML templates

#The "general information" inputs on the index page
# see index.html to see how these are rendered
#
# Types of questions.
# - Checkboxes (checkbox)
# - Radio buttons (radio)
# - Text entry (text)
# -
#
index_general_inputs = {
	"inputs": [
		{"label": "Test Item 1", "id": "t1"},
		{"label": "Test Item 2", "id": "t2"},
		{"label": "Test Item 3", "id": "t3"},
	],
	"questions": [
		{
			"label": "Please answer this queston?",
			"type": "radio",
			"other_id": "14",
		 	"inputs": [
		 		{"label":"Answer1", "id":"11"},
		 		{"label":"Answer2", "id":"12"},
		 		{"label":"Other", "id":"13"}
		 	]
		}
	]
}

