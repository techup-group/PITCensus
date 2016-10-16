import pygal
from pygal.style import DarkSolarizedStyle
import pymongo

def get_charts():

	client = pymongo.MongoClient('localhost', 27017)
	db = client["pit"]
	collection = db["2017"]
	cursor = collection.find()
	hotel_cursor = collection.find({"where_stay_last": "hotel"})
	notFit_cursor = collection.find({"where_stay_last": "notFit"})

	pie_chart = pygal.Pie()
	pie_chart.title = 'Where did the homeless spend last night? (in %)'
	pie_chart.add('Hotel', hotel_cursor.count())
	pie_chart.add('A place not fit for habitation', notFit_cursor.count())
	return pie_chart