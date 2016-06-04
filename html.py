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
		{"label": "Test Item 3", "id": "t4"}
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
		},
		{
		    "label":"Please tell me your first name:", 
		    "type":"text",
		    "id":"21"
		},
		{
		    "label":"Please tell me the first 3 letters of your last name:",
		    "id":"31"
		    "type":"text"
		},
    	{ 	"label":"Last 4 of your SSN:", 
    		"id":"41"
    		"type":"text" 
		},
		{
		    "label":"What is your date of birth? or Age",
		    "type":"radio",
		    "other_id":"54",
		    "inputs":[
		        { "label":"DOB", "id":"51" },
		        { "label":"Age", "id":"52" },
		        { "label":"Other", "id":"53" }
		    ]
		},
		{
		    "label":"Are you:",
		    "type":"radio",
		    "other_id":"65"
		    "inputs": [
		        { "label":"Male", "id":"61" },
		        { "label":"Female", "id":"62" },
		        { "label":"Transgender M to F", "id":"63" },
		        { "label":"Transgender F to M", "id":"64" }
		    ]
		},
		{
		    "label":"Are you Hispanic or Latino?",
		    "type":"radio",
		    "inputs":[
		        { "label":"Yes", "id":"71" },
		        { "label":"No",  "id":"72" }
		    ]
		}
	]
}

