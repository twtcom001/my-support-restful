# coding:utf-8
import json
from datetime import datetime
from flask import jsonify, abort, request 
from flask_restful import Resource, fields, reqparse
from flask import render_template

from ..models import Permission, User, Logs, Plants, db, Account
from ..decorator import acao_auth
from . import main


@main.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@main.route('/auth', methods=['GET','POST'])
@acao_auth
def auth():
	if request.args.get('username'):
		user = User.query.filter_by(username=request.args.get('username')).first()
	else:
		abort(401)
	if user is not None and user.verify_password(request.args.get('password')):
		#login_user(user)
		user.last_login = datetime.now()
		db.session.add(user)
		db.session.commit()
		token = user.generate_auth_token()
		return jsonify({'auth':'valid', 'token':token})
	else:
		return jsonify({'auth':'invalid'})

