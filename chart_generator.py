import pygal
from pygal.style import DarkSolarizedStyle
import pymongo

def get_last_night_chart():

	client = pymongo.MongoClient('localhost', 27017)
	db = client["pit"]
	collection = db["2017"]
	cursor = collection.find()
	hotel_cursor = collection.find({"where_stay_last": "hotel"})
	notFit_cursor = collection.find({"where_stay_last": "notFit"})
	psychiatricFacility_cursor = collection.find({"where_stay_last": "psychiatric90"})
	substanceAbuse_cursor = collection.find({"where_stay_last": "substanceAbuse90"})
	hospital_cursor = collection.find({"where_stay_last": "hospital90"})
	jail_cursor = collection.find({"where_stay_last": "jail90"})
	transitionalHousing_cursor = collection.find({"where_stay_last": "transitionalHousingName"})
	emergencyHousing_cursor = collection.find({"where_stay_last": "emergencyShelterName"})
	nonHomeless_cursor = collection.find({"where_stay_last": "nonHomelessSituation"})

	pie_chart = pygal.Pie()
	pie_chart.title = 'Where did the homeless spend last night? (in %)'
	pie_chart.add('A hotel', hotel_cursor.count())
	pie_chart.add('A place not fit for habitation', notFit_cursor.count())
	pie_chart.add('A psychiatric facility', psychiatricFacility_cursor.count())
	pie_chart.add('A substance abuse facility', substanceAbuse_cursor.count())
	pie_chart.add('A hospital', hospital_cursor.count())
	pie_chart.add('A jail', jail_cursor.count())
	pie_chart.add('Transitional housing', transitionalHousing_cursor.count())
	pie_chart.add('An emergency shelter', emergencyHousing_cursor.count())
	pie_chart.add('A nonhomeless situation', nonHomeless_cursor.count())
	return pie_chart


def get_veteran_chart():

	client = pymongo.MongoClient('localhost', 27017)
	db = client["pit"]
	collection = db["2017"]
	cursor = collection.find()
	yes_cursor = collection.find({"veteran_status": "yes"})
	no_cursor = collection.find({"veteran_status": "no"})
	
	pie_chart = pygal.Pie()
	pie_chart.title = 'How many of the homeless are veterans? (in %)'
	pie_chart.add('Veteran', yes_cursor.count())
	pie_chart.add('Not a veteran', no_cursor.count())
	return pie_chart