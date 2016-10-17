#!/usr/bin/env python
import database
import pygal
from pygal.style import DarkSolarizedStyle

def get_last_night_chart():
	labels = {
		"hotel": "Hotel",
		"notFit": "A place not fit for habitation",
		"psychiatric90": "A psychiatric facility",
		"substanceAbuse90": "A substance abuse facility",
		"hospital90": "Hospital",
		"jail90": "Jail",
		"transitionalHousingName": "Transitional housing",
		"emergencyShelterName": "An emergency shelter",
		"nonHomelessSituation": "Not homeless"
	}
	return get_pie_chart('Where did the homeless spend last night? (in %)', "where_stay_last", labels)


def get_veteran_chart():
	labels = {
		"yes": "Veteran",
		"no": "Not Veteran"
	}
	return get_pie_chart('How many of the homeless are veterans? (in %)', "veteran_status", labels)

# Returns a pie chart counting answers for "surveyQuesion"
# answerLabels: Dictionary for human-readable labels from survey answer keys
def get_pie_chart(title, surveyQuesion, answerLabels):
	pie_chart = pygal.Pie()
	pie_chart.title = title

	collection = database.getCurrentCollection()
	results = collection.find({surveyQuesion:{'$exists': True}})
	for result in results:
		answer = result[surveyQuesion][0]  #TODO: Questions with multiple answers?
		label = answerLabels[answer] if answer in answerLabels else answer
		count = collection.find({surveyQuesion: answer}).count()
		pie_chart.add(label, count)

	return pie_chart	