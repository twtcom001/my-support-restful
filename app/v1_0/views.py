# coding:utf-8

import json
from flask import jsonify, abort, request 
from flask.ext.restful import Resource, fields, reqparse
from functools import wraps

from ..models import Permission, User, Logs, Plants, db
from ..decorator import acao_auth
from . import v1_0




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
