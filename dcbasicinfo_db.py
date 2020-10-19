from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Door_Centerdb?retryWrites=true&w=majority')
	db = con.Door_Centerdb
	col = db.dcbasic_info



def get_dcbasicinfo_details():
	global col
	connect_db()
	dcbasicinfo_from_db = col.find({})
	return dcbasicinfo_from_db

def save_dcbasicinfo_details(dbbasic_info):
	global col
	connect_db()
	col.insert(dbbasic_info)
	return "saved Successfully"


def get_one_dcbasicinfo_details(dcbifo_id):
	global col
	connect_db()
	dcbdata_from_db = col.find({"_id": ObjectId(dcbifo_id)})
	return dcbdata_from_db



def update_one_record(dcbifo_id, dcbinfoRecords):
    global col
    connect_db()    
    col.update_one({"_id": ObjectId(dcbifo_id)}, {'$set' :{'Dc_number':dcbinfoRecords["Dc_number"], 'Dc_name':dcbinfoRecords["Dc_name"], 'Dc_address':dcbinfoRecords["Dc_address"], 'Dc_city':dcbinfoRecords["Dc_city"], 'Dc_state':dcbinfoRecords["Dc_state"], 'Dc_zip':dcbinfoRecords["Dc_zip"], 'Dc_country':dcbinfoRecords["Dc_country"], 'Dc_phone':dcbinfoRecords["Dc_phone"], 'Dc_email':dcbinfoRecords["Dc_email"], 'AmarrDistMgrFirstname':dcbinfoRecords["AmarrDistMgrFirstname"], 'AmarrDistMgrLastname':dcbinfoRecords["AmarrDistMgrLastname"], 'AmarrDistMgrPhone':dcbinfoRecords["AmarrDistMgrPhone"], 'AmarrDistMgrEmail':dcbinfoRecords["AmarrDistMgrEmail"], 'SmFirstname':dcbinfoRecords["SmFirstname"], 'SmLastname':dcbinfoRecords["SmLastname"], 'SmPhone':dcbinfoRecords["SmPhone"], 'SmEmail':dcbinfoRecords["SmEmail"]} })
    return


def search_doorcenter_by_id(id):
   global col_installer
   connect_db() 
   searched_data = col.find({'Dc_number':str(id)})
   return searched_data


def search_doorcenter_by_state(state):
   global col_installer
   connect_db() 
   searched_state_data = col.find({'Dc_state':state})
   return searched_state_data


def search_doorcenter_by_city(city):
   global col_installer
   connect_db() 
   searched_city_data = col.find({'Dc_city':city})
   return searched_city_data