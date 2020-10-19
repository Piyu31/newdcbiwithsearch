from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import dcbasicinfo_db

app = Flask(__name__)


app.secret_key="gyw79wvdysbt63e61ifbt56"


@app.route("/")
def index():
	#get all data from db
	dbbasic_info = dcbasicinfo_db.get_dcbasicinfo_details()
	dcbasicinfo_list = []
	for i in dbbasic_info:
		dcbasicinfo_list.append(i)
	return render_template('form.html', dcbasicinfolist = dcbasicinfo_list )


def setData():
	#Empty List
	dcbinfoRecords = {}
	#request data from UI
	#Dc info
	Dc_number = request.form['dcnum']
	Dc_name = request.form['dcname']
	Dc_address = request.form['dcaddr']
	Dc_city = request.form['dccity']
	Dc_state =  request.form['dcstate']
	Dc_zip =  request.form['dczip']
	Dc_country =  request.form['dccountry']
	Dc_phone =  request.form['dcphone']
	Dc_email =  request.form['dcemail']
	#set data to the Empty list
	dcbinfoRecords ["Dc_number"]=Dc_number
	dcbinfoRecords ["Dc_name"]=Dc_name
	dcbinfoRecords ["Dc_address"]=Dc_address
	dcbinfoRecords ["Dc_city"]=Dc_city
	dcbinfoRecords ["Dc_state"]=Dc_state
	dcbinfoRecords ["Dc_zip"]=Dc_zip
	dcbinfoRecords ["Dc_country"]=Dc_country
	dcbinfoRecords ["Dc_phone"]=Dc_phone
	dcbinfoRecords ["Dc_email"]=Dc_email
	#AmarrDistrict manager
	AmarrDistMgrFirstname = request.form['admfirstname']
	AmarrDistMgrLastname = request.form['admlastname']
	AmarrDistMgrPhone = request.form['admphone']
	AmarrDistMgrEmail =  request.form['admemail']
	#set data to the empty list
	dcbinfoRecords ["AmarrDistMgrFirstname"] = AmarrDistMgrFirstname
	dcbinfoRecords ["AmarrDistMgrLastname"] = AmarrDistMgrLastname
	dcbinfoRecords ["AmarrDistMgrPhone"] = AmarrDistMgrPhone
	dcbinfoRecords ["AmarrDistMgrEmail"] = AmarrDistMgrEmail
	#Sales manager
	SmFirstname = request.form['smfirstname']
	SmLastname = request.form['smlastname']
	SmPhone = request.form['smphone']
	SmEmail =  request.form['smemail']
	#set data to the empty list
	dcbinfoRecords ["SmFirstname"] = SmFirstname
	dcbinfoRecords ["SmLastname"] = SmLastname
	dcbinfoRecords ["SmPhone"] = SmPhone
	dcbinfoRecords ["SmEmail"] = SmEmail
	
	return dcbinfoRecords 

@app.route("/", methods=['POST'])
def update_dcbasicinfo():
	dcbinfoRecords = setData()
	#print records in cmd
	print(dcbinfoRecords)
	dcbasicinfo_db.save_dcbasicinfo_details(dcbinfoRecords)
	return redirect(url_for('index'))


@app.route("/update", methods=['POST'])
def update_dcbasicinfo_records():
	dcbinfoRecords = setData()
	#print records in cmd
	print(dcbinfoRecords)
	print(request.form['id'])
	#send to db
	dcbinfoid=request.form['id']
	dcbasicinfo_db.update_one_record(dcbinfoid, dcbinfoRecords)
	return redirect(url_for('index'))



@app.route("/edit/<dcbifo_id>", methods=['POST'])
def edit_Record(dcbifo_id):
    dcbinfoi = dcbifo_id
    one_dcb_info = dcbasicinfo_db.get_one_dcbasicinfo_details(dcbifo_id)
    return render_template('edit.html', dcbasicinfolist = one_dcb_info)

doorcenters = []
search_results_activated_doorcenters = False

@app.route("/doorcenter", methods=['GET'])
def doorcenterWrapper():
   global doorcenters
   global search_results_activated_doorcenters
   doorcenters_list = []
   if search_results_activated_doorcenters:
       doorcenters_list = doorcenters
   else:
       cursor = dcbasicinfo_db.get_dcbasicinfo_details()
       for doc in cursor:
           doorcenters_list.append(doc)
   search_results_activated_doorcenters = False
   return render_template('form.html',  dcbasicinfolist = doorcenters_list)


@app.route('/doorcenter/searchbyid', methods=['POST'])
def searchDoorcentersByDcNum():
   global doorcenters
   global search_results_activated_doorcenters
   doorcenters_list = []
   doorcenter_id = request.form['searchbydcnumber']
   door_list = dcbasicinfo_db.search_doorcenter_by_id(int(doorcenter_id))
   for door in door_list:
       doorcenters_list.append(door)
   print(doorcenters_list)
   doorcenters = doorcenters_list
   search_results_activated_doorcenters = True
   return redirect(url_for('doorcenterWrapper'))


@app.route('/doorcenter/searchbystate', methods=['POST'])
def searchDoorcentersrByState():
   global doorcenters
   global search_results_activated_doorcenters
   doorcenters_list = []
   state = request.form['searchbystate']
   door_list = dcbasicinfo_db.search_doorcenter_by_state(state)
   for door in door_list:
       doorcenters_list.append(door)
   print(doorcenters_list)
   doorcenters = doorcenters_list
   search_results_activated_doorcenters = True
   return redirect(url_for('doorcenterWrapper'))


@app.route('/doorcenter/searchbycity', methods=['POST'])
def searchDoorcentersrByCity():
   global doorcenters
   global search_results_activated_doorcenters
   doorcenters_list = []
   city = request.form['searchbycity']
   door_list = dcbasicinfo_db.search_doorcenter_by_city(city)
   for door in door_list:
       doorcenters_list.append(door)
   print(doorcenters_list)
   doorcenters = doorcenters_list
   search_results_activated_doorcenters = True
   return redirect(url_for('doorcenterWrapper'))






if __name__ == '__main__':
	app.run(debug=True)

