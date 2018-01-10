# coding:utf-8

import json
from flask import jsonify, abort, request 
from flask_restful import Resource, fields, reqparse
from functools import wraps


from ..models import Permission, User, Logs, Plants, db, Account
from ..decorator import acao_auth
from . import v1_0



#User 接口
@v1_0.route('/users', methods=['GET'])
@acao_auth
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
	result ={"list":userlist,'total':usercount,'page':page,'size':size}
	return jsonify(result)


@v1_0.route('/users', methods=['POST'])
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

	return jsonify({'user':'用户增加成功'})

@v1_0.route('/users/<int:user_id>', methods=['PUT'])
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
	return jsonify({'user':'用户数据更新'})



@v1_0.route('/users/<int:user_id>', methods=['GET'])
@acao_auth
def get_user(user_id):
	userlist = []
	user = User.query.filter_by(id=user_id).first()
	if not user:
		abort(404)
	user_dict = user.__dict__
	user_dict.pop('_sa_instance_state')
	userlist.append(user_dict)
	return jsonify(userlist)

@v1_0.route('/users/del/<int:user_id>', methods=['GET'])
def del_user(user_id):
	user = User.query.filter_by(id=user_id).first()	
	if not user:
		abort(404)
	if ( user_id == 1 ):
		return abort(403)
	else:
		db.session.delete(user)
		db.session.commit()
		return jsonify({'user':'用户删除成功'})

# Account 接口
@v1_0.route('/account', methods=['GET'])
@acao_auth
def get_account(page=1,size=10):
	if request.args.get('page'):
		page = int(request.args.get('page'))
	if request.args.get('size'):
		size = int(request.args.get('size'))
	if request.args.get('src'):
		src = int(request.args.get('src'))
		records = Account.query.filter(Account.src == src).offset((page-1)*size).limit(size)
		total = Account.query.filter(Account.src == src)

	else:
		src = ''
		records = Account.query.offset((page-1)*size).limit(size)
		total = Account.query.all()

	recordtotal = 0
	for i in total:
		recordtotal = recordtotal+i.total

	recordlist = []
	for i in records:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		recordlist.append(i_dict)
	count = len(recordlist)

	result ={"list":recordlist,'total':count, 'count':recordtotal,'src':src,'page':page,'size':size}
	return jsonify(result)

@v1_0.route('/account', methods=['POST'])
def add_account():
	data =request.data
	if not data or 'date' not in data or 'total' not in data \
		or 'src' not in data:
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
			comment=j_data['comment']
			)
	db.session.add(account)
	db.session.commit()

	return jsonify({'account':'数据增加成功'})

@v1_0.route('/account/<int:account_id>', methods=['PUT'])
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
	db.session.commit()
	return jsonify({'account':'数据更新成功'})

@v1_0.route('/account/del/<int:account_id>', methods=['GET'])
def del_account(account_id):
	account = Account.query.filter_by(id=account_id).first()	
	if not account:
		abort(404)
	else:
		db.session.delete(account)
		db.session.commit()
		return jsonify({'account':'收支删除成功'})

