# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from datetime import datetime
from flask import jsonify, abort, request, g
from flask_restful import Resource, fields, reqparse
from functools import wraps
from sqlalchemy import or_


from ..models import db, Address, Plants
from ..decorator import acao_auth, auth_token
from . import v2_1
from app import auth

#Address 接口
@v2_1.route('/address', methods=['GET'])
@acao_auth
@auth_token
def get_addresslist(page=1, size=10, keys=''):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	addresslist = []
	if  request.args.get('keys') == '' or request.args.get('keys') == None:
		addresscount =Address.query.filter(id>0).count()
		address = Address.query.offset((page-1)*size).limit(size)
	else:
		keys = str(request.args.get('keys'))
		addresscount =Address.query.filter(or_(Address.name.like('%'+keys+'%'),Address.address.like('%'+keys+'%'),Address.mobile.like('%'+keys+'%'))).count()
		address = Address.query.filter(or_(Address.name.like('%'+keys+'%'),Address.address.like('%'+keys+'%'),Address.mobile.like('%'+keys+'%'))).offset((page-1)*size).limit(size)		

	for i in address:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		addresslist.append(i_dict)
	result ={"code":20000,"data":{"list":addresslist,'total':addresscount,'page':page,'size':size}}
	return jsonify(result)
@v2_1.route('/address', methods=['POST'])
@acao_auth
@auth_token
def add_address():
	data =request.data
	
	if not data or 'name' not in data or 'address' not in data \
		or 'mobile' not in data or 'address_type' not in data:
		abort(404)
	j_data =  json.loads(data)
	address = Address(
			name=j_data['name'],
			address=j_data['address'],
			address_type=j_data['address_type'],
			mobile=j_data['mobile'],
			telephone=j_data['telephone'],
			comment=j_data['comment']
			)
	db.session.add(address)
	db.session.commit()
	
	return jsonify({"code":20000})

@v2_1.route('/address/<int:address_id>', methods=['PUT'])
@acao_auth
@auth_token
def update_address(address_id):
	data =request.data
	address = Address.query.filter_by(id=address_id).first()	
	if not address :
		abort(404)
	j_data =  json.loads(data)
	if 'name' in data and j_data['name'] != "":
		address.name = j_data['name']
	if 'address' in data and j_data['address'] != "":
		address.address = j_data['address']
	if 'address_type' in data and j_data['address_type'] != "":
		address.address_type = j_data['address_type']
	if 'mobile' in data and j_data['mobile'] != "":
		address.mobile = j_data['mobile']
	if 'telephone' in data and j_data['telephone'] != "":
		address.telephone = j_data['telephone']
	if 'comment' in data and j_data['comment'] != "":
		address.comment = j_data['comment']
	db.session.commit()
	return jsonify({"code":20000})

@v2_1.route('/address/<int:address_id>', methods=['GET'])
@auth_token
def get_address(address_id):
	addresslist = []
	address = Address.query.filter_by(id=address_id).first()
	if not address:
		abort(404)
	address_dict = address.__dict__
	address_dict.pop('_sa_instance_state')
	addresslist.append(address_dict)
	return jsonify(addresslist)

@v2_1.route('/address/del/<int:address_id>', methods=['GET'])
@auth_token
def del_address(address_id):
	address = Address.query.filter_by(id=address_id).first()	
	if not address:
		abort(404)
	db.session.delete(address)
	db.session.commit()
	return jsonify({"code":20000})

# Plant 接口
@v2_1.route('/plant', methods=['GET'])
@acao_auth
@auth_token
def get_plantlist(page=1, size=10, keys=''):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	resultlist = []
	if  request.args.get('keys') == '' or request.args.get('keys') == None:
		resultcount =Plants.query.filter(id>0).count()
		result = Plants.query.offset((page-1)*size).limit(size)
	else:
		keys = str(request.args.get('keys'))
		resultcount =Plants.query.filter(or_(Plants.genus.like('%'+keys+'%'),Plants.icbn_name.like('%'+keys+'%'),Plants.chinese_name.like('%'+keys+'%'),Plants.sn.like('%'+keys+'%'))).count()
		result = Plants.query.filter(or_(Plants.genus.like('%'+keys+'%'),Plants.icbn_name.like('%'+keys+'%'),Plants.chinese_name.like('%'+keys+'%'),Plants.sn.like('%'+keys+'%'))).offset((page-1)*size).limit(size)		

	for i in result:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		resultlist.append(i_dict)
	result ={"code":20000,"data":{"list":resultlist,'total':resultcount,'page':page,'size':size}}
	return jsonify(result)
@v2_1.route('/plant', methods=['POST'])
@acao_auth
@auth_token
def add_plant():
	data =request.data
	
	if not data or 'genus' not in data or 'sn' not in data:
		abort(404)
	j_data =  json.loads(data)
	result = Plants(
			genus=j_data['genus'],
			icbn_name=j_data['icbn_name'],
			chinese_name=j_data['chinese_name'],
			osn=j_data['osn'],
			sn=j_data['sn'],
			summary=j_data['summary']
			)
	db.session.add(result)
	db.session.commit()
	
	return jsonify({"code":20000})

@v2_1.route('/plant/<int:plant_id>', methods=['PUT'])
@acao_auth
@auth_token
def update_plant(plant_id):
	data =request.data
	result = Plants.query.filter_by(id=plant_id).first()	
	if not result :
		abort(404)
	j_data =  json.loads(data)
	if 'genus' in data and j_data['genus'] != "":
		result.genus = j_data['genus']
	if 'icbn_name' in data and j_data['icbn_name'] != "":
		result.icbn_name = j_data['icbn_name']
	if 'chinese_name' in data and j_data['chinese_name'] != "":
		result.chinese_name = j_data['chinese_name']
	if 'osn' in data and j_data['osn'] != "":
		result.osn = j_data['osn']
	if 'sn' in data and j_data['sn'] != "":
		result.sn = j_data['sn']
	if 'summary' in data and j_data['summary'] != "":
		result.summary = j_data['summary']
	db.session.commit()
	return jsonify({"code":20000})

@v2_1.route('/plant/<int:plant_id>', methods=['GET'])
@auth_token
def get_plant(plant_id):
	resultlist = []
	result = Plants.query.filter_by(id=plant_id).first()
	if not result:
		abort(404)
	result_dict = result.__dict__
	result_dict.pop('_sa_instance_state')
	resultlist.append(result)
	return jsonify(resultlist)

@v2_1.route('/plant/del/<int:plant_id>', methods=['GET'])
@auth_token
def del_plant(plant_id):
	result = Plants.query.filter_by(id=plant_id).first()	
	if not result:
		abort(404)
	db.session.delete(result)
	db.session.commit()
	return jsonify({"code":20000})
