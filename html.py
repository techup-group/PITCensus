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
	"qualification": [
		{
		    "label": "Have you completed this survey earlier today?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Yes", "id":"1000"},
		        {"label":"No", "id":"1001"}
			]
		},
		{
		    "label": "Are you currently homeless?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Yes", "id":"1100"},
		        {"label":"No", "id":"1101"}
			]
		},
		{
		    "label": "Where did you stay last night?",
		    "inputs": [
		        {"label":"Place not meant for habitation (car, street, abandoned building, etc.)","type":"radio", "id":"1201"},
		        {"label":"Emergency shelter (ES)","type":"radio", "id":"1202"},
				{"label":"ES Name:", "type":"text", "id":"1203"},
		        {"label":"Transitional housing for homeless (TH)","type":"radio", "id":"1204"},
				{"label":"TH Name:", "type":"text", "id":"1205"},
				{"label":"Hotel/Motel paid for by an agency or organization","type":"radio", "id":"1206"},
				{"label":"Psychiatric facility","type":"radio", "id":"1207"},
				{"label":"Substance abuse treatment facility","type":"radio", "id":"1208"},
				{"label":"Hospital","type":"radio", "id":"1209"},
				{"label":"Jail, prison, detention facility","type":"radio", "id":"1210"},
				{"label":"For Less than 90 Days","type":"checkbox", "id":"1211"},
				{"label":"For 90 Days or more","type":"checkbox", "id":"1212"}
			]
		}	
	],
	"questions": [
		{
		    "label":"Please tell me your first name:", 
		    "type":"text",
		    "id":"21"
		},
		{
		    "label":"Please tell me the first 3 letters of your last name:",
		    "id":"31",
		    "type":"text"
		},
    	{ 	"label":"Last 4 of your SSN:", 
    		"id":"41",
    		"type":"text" 
		},
		{
		    "label":"What is your date of birth? or Age",
		    "type":"radio",
		    "inputs":[
		        { "label":"DOB", "id":"51" },
		        { "label":"Age", "id":"52" },
		        { "label":"Other", "id":"53" },
		        { "label":"", "type": "text", "id":54}
		    ]
		},
		{
		    "label":"Are you:",
		    "type":"radio",
		    "other_id":"65",
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
		},
		{
		    "label": "What is your race?(Please circle Primary Race if more than one is indicated):",
		    "type": "radio",
		    "inputs": [
		        {"label":"American Indian/Alaskan Native", "id":"41"},
		        {"label":"Asian", "id":"42"},
		        {"label":"Black/African American", "id":"43"},
				{"label":"Native Hawaiian/Other Pacific Islander", "id":"43"}
			]
		},
		{
		    "label": "How long have you been in this episode of homelessness?",
		    "type": "radio",
		    "other_id": "14",
		    "inputs": [
		        {"label":"1 week or less", "id":"51"},
		        {"label":"more than 1 week, but less than 1 month", "id":"52"},
		        {"label":"1 - 3 months", "id":"53"},
				{"label":"more than 3 months, but less than 1 year", "id":"54"},
				{"label":"1 year or longer", "id":"53"}
		    ]
		},
		{
		    "label": "How many times have you been on the streets, Emergency Shelter, or Safe Haven in the past three years including today?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Never in the 3 years", "id":"61"},
		        {"label":"One Time", "id":"62"},
		        {"label":"Two Times", "id":"63"},
		        {"label":"Three Times", "id":"64"},        
		        {"label":"Four or More Times", "id":"65"}
			]
   		},
		{
		    "label": "Total number of months you have been homeless on the street, Emergency Shelter, or Safe Haven in the past three years?",
		    "type": "text"
		},
		{
		    "label": "How long have you been staying in Hillsborough County?",
		    "type": "radio",
		    "inputs": [
		        {"label":"1 week or less", "id":"71"},
		        {"label":"More than 1 week, but less than 1 month", "id":"72"},
		        {"label":"More than 1 week, but less than 1 month", "id":"73"},
				{"label":"1 to 3 months", "id":"74"},
				{"label":"More than 3 months, but less than 1 year", "id":"75"},
				{"label":"1 year or longer", "id":"76"}
			]
		},
		{
		    "label": "What is the primary cause of your homelessness?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Employment/financial reasons", "id":"81"},
		        {"label":"Family problems", "id":"82"},
		        {"label":"Recent immigration", "id":"83"},
		        {"label":"Housing issues", "id":"84"},
		        {"label":"Natural/other disasters", "id":"85"},
		        {"label":"Medical/disability problems", "id":"86"},
		        {"label":"Other", "id":"87"},
		        {"label":"", "id":"88"}
		    ]
		},
		{
		    "label": "Were you ever in foster care as a child?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Yes", "id":"91"},
		        {"label":"No", "id":"92"}
		    ]
		},
		{
		    "label": "Do you have a disabling condition?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Yes", "id":"101"},
		        {"label":"No (If No, skip next question)", "id":"102"}
		    ]
		},
		{
		    "label": "What type of disabling condition do you have? (you may select more than one condition)?",
		    "type": "checkbox",
		    "inputs": [
		        {"label":"Physical", "id":"110"},
		        {"label":"Developmental", "id":"111"},
		        {"label":"Mental health", "id":"112"},
		        {"label":"Alcohol Abuse", "id":"113"},
		        {"label":"Drug Abuse", "id":"114"},
		        {"label":"HIV/AIDS", "id":"115"}
		    ]
		},
		{
		    "label": "Have you ever served on Active Duty in the US Military?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Yes", "id":"120"},
		        {"label":"No(If \"No\", skip next question)", "id":"121"}
		    ]
		},
		{
		    "label": "What Branch of the Military did you serve?",
		    "type": "radio",
		    "inputs": [
		        {"label":"Army", "id":"130"},
		        {"label":"Air Force", "id":"131"},
		        {"label":"Navy", "id":"132"},
		        {"label":"Marines", "id":"133"},
		        {"label":"Coast Guard", "id":"134"}
		    ]
		},
		{
		    "label": "Do you receive any income?",
		    "type": "multipart",
		    "inputs": [
		        {"label":"Yes  (if yes, check all sources that apply?)", "type":"radio", "id":"140"},
				{"label":"No Income", "type":"radio", "id":"141"},
		        {"label":"Amount $ /month (Gross)", "type":"text", "id":"142"},
		        {"label":"Earned income", "type":"checkbox", "id":"143"},
		        {"label":"Alimony", "type":"checkbox", "id":"144"},
		        {"label":"SSA retirement", "type":"checkbox", "id":"145"},
		        {"label":"VA Disability Pension (NON-service connected)", "type":"checkbox", "id":"146"},
		        {"label":"SSI", "type":"checkbox", "id":"147"},
		        {"label":"Workers' Comp", "type":"checkbox", "id":"148"},
		        {"label":"Pension/Retirement Income", "type":"checkbox", "id":"149"},
		        {"label":"TANF", "type":"checkbox", "id":"150"},
		        {"label":"VA Disability Comp (Service Connected)", "type":"checkbox", "id":"151"},
		        {"label":"SSDI", "type":"checkbox", "id":"152"},
		        {"label":"Private disability insurance", "type":"checkbox", "id":"153"},
		        {"label":"Unemployment", "type":"checkbox", "id":"154"},
		        {"label":"Child support", "type":"checkbox", "id":"155"},
		        {"label":"SSDI", "type":"checkbox", "id":"156"},
		        {"label":"Other source", "type":"text", "id":"157"}
		    ]
		}
	]
}

