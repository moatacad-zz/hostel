import json #json.jsonify() 
from flask import make_response,request, jsonify

from flask_httpauth import HTTPBasicAuth 

from projectapp.mymodel import Hostel,db, Merchant
#import the blueprint's instance
from . import apiobj

auth = HTTPBasicAuth() 

@auth.get_password
def get_password(username):
	deets = db.session.query(Merchant.mer_pwd).filter(Merchant.mer_username==username).first()
	if deets:
		return deets.mer_pwd
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 401)



#fetch all hostel details - GET
@apiobj.route('/list/')
def listall():
    hostels = []
    data = Hostel.query.all()
    for x in data:
        a = {}
        a['hostel'] = x.hostel_name
        a['type'] = x.hostel_type
        a['desc'] = x.hostel_desc
        hostels.append(a)
    return jsonify(hostels)


#get details of one hostel - GET
@apiobj.route('/list/<int:hostel_id>')
def listone(hostel_id): 
    data = Hostel.query.filter(Hostel.hostel_id ==hostel_id).first() 
    #form a dictionary
    data2send = {"hostel":data.hostel_name,"type":data.hostel_type}
    #convert to json using eith of json.dumps() or jsonify
    rsp = make_response(json.dumps(data2send),200)
    rsp.headers['Content-Type']="application/json"
    return rsp



#add new hostel details - POST
@apiobj.route('/addnew/',methods=['POST'])
@auth.login_required
def addnew():
    if request.is_json: #confirm request type
        hostel_deets = request.get_json() #python dict
        hostelname = hostel_deets['hostelname']  #use hostel_deets.get('hostelname')  for graceful degradation
        desc = hostel_deets['description']
        hosteltype = hostel_deets['type']

        host = Hostel(hostel_name=hostelname, hostel_desc=desc,hostel_type=hosteltype)
        db.session.add(host)
        db.session.commit()
        ret = {"status":1, "msg":'Hostel added'} #always send consistent messages for the machine on the other end
    else:
        ret = {"status":0, "msg":'Try Again'}    
    return jsonify(ret)

#delete hostel details - DELETE
@apiobj.route('/deletehostel/<int:hostel_id>', methods=['DELETE'])
def deletehostel(hostel_id): 
    return 'Hostel Deleted!'

#update hostel details PUT
@apiobj.route('/updatehostel/<int:hostel_id>',methods=['PUT'])
def updatehostel(hostel_id): 

    return 'Hostel Updated!'