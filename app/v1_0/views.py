# coding:utf-8

import json
from flask import jsonify, abort, request
from flask.ext.restful import Resource, fields, reqparse

from ..models import Permission, User, Logs, Plants, db
from . import v1_0

@v1_0.route('/users', methods=['GET'])
def get_userlist():
	userlist = []
	user = User.query.filter(id>0)
	for i in user:
		i_dict = i.__dict__
		i_dict.pop('_sa_instance_state')
		userlist.append(i_dict)
	return jsonify(userlist)

@v1_0.route('/users', methods=['POST'])
def add_user():
	data =request.data
	if not data or 'email' not in data or 'username' not in data \
		or 'password' not in data:
		abort(404)
	j_data =  json.loads(data)
	if 'role_id' not in data:
		role_id = 1
	else:
		role_id = j_data['role_id']

	user = User(
			email=j_data['email'],
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
	if not user or 'email' in data:
		abort(404)
	j_data =  json.loads(data)
	if 'username' in data:
		user.username = j_data['username']
	if 'password' in data:
		user.password = j_data['password']
	db.session.commit()
	return jsonify({'user':'用户数据更新'})

@v1_0.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	user = User.query.filter_by(id=user_id).first()	
	if not user:
		abort(404)
	user_dict = user.__dict__
	user_dict.pop('_sa_instance_state')
	return jsonify(user_dict)

@v1_0.route('/users/<int:user_id>', methods=['DELETE'])
def del_user(user_id):
	user = User.query.filter_by(id=user_id).first()	
	if not user:
		abort(404)
	if ( user_id == 1 ):
		return jsonify({'user':"管理员禁止删除!"})
	else:
		db.session.delete(user)
		db.session.commit()
		return jsonify({'user':'用户删除成功'})
