# coding:utf-8

import json
from datetime import datetime
from flask import jsonify, abort, request, g
from flask_restful import Resource, fields, reqparse
from functools import wraps


from ..models import Permission, User, Logs, Plants, db, Account, Dict
from ..decorator import acao_auth, auth_token
from . import v2_0
from app import auth
# 登录接口
# User 接口
# Account 接口

# 登录接口
@v2_0.route('/login', methods=['POST'])
@acao_auth
def login():
	data =request.data
	if 'username' not in data or 'password' not in data:
		return jsonify({"code":40100})
	else:
		j_data =  json.loads(data)
		username = j_data['username']
		user = User.query.filter_by(username=username).first()
		if user.verify_password(j_data['password']):
			user.last_login = datetime.now()
			db.session.add(user)
			db.session.commit()
			token = user.generate_auth_token()
			return jsonify({"code":20000,"data":{"token":token}})
		else:
			return jsonify({"code":40100})


@v2_0.route('/logout', methods=['POST'])
def admin_logout():
	data =request.data
	return jsonify({"code":20000})

@v2_0.route('/info', methods=['GET'])
def info():
	if request.args.get('token'):
		user = User.verify_auth_token(request.args.get('token'))
		return jsonify({"code":20000,"data":{"roles":user.role_id,"role":user.role_id,"name":user.username,"avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"}})
	else:
		return jsonify({"code":40})

#User 接口
@v2_0.route('/users', methods=['GET'])
@acao_auth
@auth_token
def get_userlist(page=1,size=10):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	userlist = []
	usercount =User.query.filter(id>0).count()
	user = User.query.offset((page-1)*size).limit(size)
	for i in user:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		userlist.append(i_dict)
	result ={"code":20000,"data":{"list":userlist,'total':usercount,'page':page,'size':size}}
	return jsonify(result)


@v2_0.route('/users', methods=['POST'])
@acao_auth
#@auth_token
def add_user():
	data =request.data
	
	if not data or 'nickname' not in data or 'username' not in data \
		or 'password' not in data:
		abort(404)
	j_data =  json.loads(data)
	if 'role' not in data:
		role_id = 1
	else:
		role_id = j_data['role']

	user = User(
			nickname=j_data['nickname'],
			username=j_data['username'],
			)
	user.password = j_data['password']
	user.role_id = role_id
	db.session.add(user)
	db.session.commit()
	
	return jsonify({"code":20000})

@v2_0.route('/users/<int:user_id>', methods=['PUT'])
@auth_token
def update_user(user_id):
	data =request.data
	user = User.query.filter_by(id=user_id).first()	
	if not user or not 'username' in data:
		abort(404)
	j_data =  json.loads(data)
	if 'nickname' in data and j_data['nickname'] != "":
		user.nickname = j_data['nickname']
	if 'password' in data and j_data['password'] != "":
		user.password = j_data['password']
	if 'role' in data and j_data['role'] != user.role_id:
		user.role_id = j_data['role']
	db.session.commit()
	return jsonify({"code":20000})



@v2_0.route('/users/<int:user_id>', methods=['GET'])
@auth_token
def get_user(user_id):
	userlist = []
	user = User.query.filter_by(id=user_id).first()
	if not user:
		abort(404)
	user_dict = user.__dict__
	user_dict.pop('_sa_instance_state')
	userlist.append(user_dict)
	return jsonify(userlist)

@v2_0.route('/users/del/<int:user_id>', methods=['GET'])
@auth_token
def del_user(user_id):
	user = User.query.filter_by(id=user_id).first()	
	if not user:
		abort(404)
	if ( user_id == 1 ):
		return abort(403)
	else:
		db.session.delete(user)
		db.session.commit()
		return jsonify({"code":20000})

# Account 接口
@v2_0.route('/account', methods=['GET'])
@acao_auth
@auth_token
def get_account(page=1,size=10):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	account_type = request.args.get('account_type')
	if request.args.get('src'):
		src = int(request.args.get('src'))
		records = Account.query.order_by(Account.id.desc()).filter(Account.src == src and Account.account_type == account_type ).offset((page-1)*size).limit(size)
		total = Account.query.filter(Account.src == src and Account.account_type == account_type )

	else:
		src = ''
		records = Account.query.order_by(Account.id.desc()).filter(Account.account_type == account_type ).offset((page-1)*size).limit(size)
		total = Account.query.filter(Account.account_type == account_type ).all()

	recordtotal = 0
	for i in total:
		recordtotal = recordtotal+i.total

	recordlist = []
	for i in records:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		recordlist.append(i_dict)
	count = len(total)
	result ={"code":20000,"data":{"list":recordlist,'total':count, 'count':recordtotal,'src':src,'page':page,'size':size}}
	return jsonify(result)

@v2_0.route('/account', methods=['POST'])
@acao_auth
@auth_token
def add_account():
	data =request.data
	if not data or 'date' not in data or 'total' not in data \
		or 'src' not in data or 'account_type' not in data:
		abort(404)
	j_data =  json.loads(data)
	if not 'comment' in data:
		j_data['comment']=''
	if j_data['date'] == '' or  j_data['total'] == '' or  j_data['src'] == '':
		abort(404)
	account = Account(
			date=j_data['date'],
			total=j_data['total'],
			src=j_data['src'],
			comment=j_data['comment'],
			account_type=j_data['account_type']
			)
	db.session.add(account)
	db.session.commit()

	return jsonify({"code":20000})

@v2_0.route('/account/<int:account_id>', methods=['PUT'])
@acao_auth
@auth_token
def update_account(account_id):
	data =request.data
	account = Account.query.filter_by(id=account_id).first()	
	if not account or not 'total' in data:
		abort(404)
	j_data =  json.loads(data)
	if account.total != j_data['total']:
		account.total = j_data['total']
	if account.date != j_data['date']:
		account.date = j_data['date']
	if account.src != j_data['src']:
		account.src = j_data['src']
	if account.comment != j_data['comment']:
		account.comment = j_data['comment']
	db.session.commit()
	return jsonify({"code":20000})

@v2_0.route('/account/del/<int:account_id>', methods=['GET'])
@acao_auth
@auth_token
def del_account(account_id):
	account = Account.query.filter_by(id=account_id).first()	
	if not account:
		abort(404)
	else:
		db.session.delete(account)
		db.session.commit()
		return jsonify({"code":20000})

#Dict 接口
@v2_0.route('/dict', methods=['GET'])
@acao_auth
@auth_token
def get_dictlist(page=1,size=10):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	dictlist = []
	dictcount =Dict.query.filter(id>0).count()
	dict = Dict.query.offset((page-1)*size).limit(size)
	for i in dict:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		dictlist.append(i_dict)
	result ={"code":20000,"data":{"list":dictlist,'total':dictcount,'page':page,'size':size}}
	return jsonify(result)
@v2_0.route('/dict', methods=['POST'])
@acao_auth
@auth_token
def add_dict():
	data =request.data
	
	if not data or 'father' not in data or 'key' not in data \
		or 'value' not in data:
		abort(404)
	j_data =  json.loads(data)
	dicts = Dict(
			father=j_data['father'],
			key=j_data['key'],
			value=j_data['value'],
			)
	db.session.add(dicts)
	db.session.commit()
	
	return jsonify({"code":20000})

@v2_0.route('/dict/<int:dict_id>', methods=['PUT'])
@acao_auth
@auth_token
def update_dict(dict_id):
	data =request.data
	dicts = Dict.query.filter_by(id=dict_id).first()	
	if not dicts :
		abort(404)
	j_data =  json.loads(data)
	if 'father' in data and j_data['father'] != "":
		dicts.father = j_data['father']
	if 'key' in data and j_data['key'] != "":
		dicts.key = j_data['key']
	if 'value' in data and j_data['value'] != "":
		dicts.value = j_data['value']
	db.session.commit()
	return jsonify({"code":20000})

@v2_0.route('/dict/<int:dict_id>', methods=['GET'])
@auth_token
def get_dict(dict_id):
	dictlist = []
	dicts = Dict.query.filter_by(id=user_id).first()
	if not user:
		abort(404)
	dicts_dict = dicts.__dict__
	dicts_dict.pop('_sa_instance_state')
	dictlist.append(dicts_dict)
	return jsonify(dictlist)

@v2_0.route('/dict/del/<int:dict_id>', methods=['GET'])
@auth_token
def del_dict(dict_id):
	dicts = Dict.query.filter_by(id=dict_id).first()	
	if not dicts:
		abort(404)
	db.session.delete(dicts)
	db.session.commit()
	return jsonify({"code":20000})

