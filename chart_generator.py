#!/usr/bin/env python
import database
import pygal
from pygal.style import Style
from collections import defaultdict

def get_last_night_chart():
	labels = {
		"hotel": "Hotel",
		"notFit": "Homeless Situation",
		"psychiatric90": "A psychiatric facility",
		"substanceAbuse90": "A substance abuse facility",
		"hospital90": "Hospital",
		"jail90": "Jail",
		"transitionalHousingName": "Transitional housing",
		"emergencyShelterName": "An emergency shelter",
		"nonHomelessSituation": "Not homeless"
	}
	return get_pie_chart('Where did the homeless spend last night?', "where_stay_last", labels)

def get_veteran_chart():
	labels = {
		"yes": "Veteran",
		"no": "Not Veteran"
	}
	return get_pie_chart('How many of the homeless are veterans?', "veteran_status", labels)

def get_cause_chart():
	labels = {
		"finance": "Financial Reasons",
		"family": "Family Problems",
		"immigration": "Recent Immigration",
		"housing": "Housing Issues",
		"disaster": "Natural/Other Disaster",
		"medical": "Medical/Disability Problems"
	}
	return get_pie_chart('What is the primary cause of homelessness?', "homelessness_cause",labels)

# Returns a pie chart counting answers for "surveyQuestion"
# answerLabels: Dictionary for human-readable labels from survey answer keys
def get_pie_chart(title, surveyQuestion, answerLabels):
	config = pygal.Config(legend_at_bottom=True)
	pie_chart = pygal.Pie(config=config)
	pie_chart.title = title
	
	for answer, count in get_survey_results(surveyQuestion).items():
		label = answerLabels[answer] if answer in answerLabels else answer
		pie_chart.add(label, count)

	return pie_chart

#Searches database for a quesion and returns a dictionary of the count of the answers
def get_survey_results(surveyQuestion):
	resultsDict = defaultdict(int)

	collection = database.getCurrentCollection()
	results = collection.find({surveyQuestion:{'$exists': True}})
	for result in results:
		answer = result[surveyQuestion][0]  #TODO: Questions with multiple answers?
		resultsDict[answer] += 1
	return resultsDict
