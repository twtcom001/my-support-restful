# coding:utf-8

import json
from datetime import datetime
from flask import jsonify, abort, request, g
from flask_restful import Resource, fields, reqparse
from functools import wraps


from ..models import Permission, User, Logs, Plants, db, Account
from ..decorator import acao_auth, auth_token
from . import v2_0
from app import auth
#User 接口
#
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

@v2_0.route('/table/list', methods=['GET'])
#@acao_auth
@auth_token
def tableslist():
	#x_token = request.headers.get('X-Token')
	return jsonify({"code":20000,"data":{"items":[
			{"id":"340000198907156578","title":"Befmh ifnolbjti paorml suiblwwnl lsf bnsyhvfje qardl snkaikwpbi pxhj bghxtn hcxtzfolb qhca yqpo.","status":"published","author":"name","display_time":"1973-10-07 12:29:07","pageviews":1694},
			{"id":"650000200504054158","title":"Pirtcth fjsouqkun qghpili nkm vlitauq sybbklng rcxevj malb qrgi eiawvyflo lepqpvitrh yhqoftvw xwbliqv rquy bldkpbeda jiuybvf.","status":"draft","author":"name","display_time":"1988-07-20 20:42:39","pageviews":3132},
			{"id":"130000199506077890","title":"Dcze nsrrjpt dofbbhe otzzmylfru giymeqg oquboqk bjdnrumk ervzexoc kmxjo kupwo niqpzaxbc klgswa csuyfwl vhgsggt grfccpiey yciuwy zewktj iksscgpr.","status":"draft","author":"name","display_time":"1997-09-06 11:31:54","pageviews":4570},
			{"id":"820000201012105015","title":"Quncgezmgi qop beynfdkpq sncworg ywiimwrokq nrozxomfa hghhpmsyn pmpfze kiojipy qsengrn xoe pvv eyheeb ehyzjlrea enbvjxqisb qjhtj jtuoltj hneohis.","status":"draft","author":"name","display_time":"1985-11-06 01:41:16","pageviews":1029},
			{"id":"410000198812038550","title":"Rav tsouqql uccgtgyl uqybtkiepg kebjdxt whpqnr ywpg nthrvgc yayygv yyixs hywchwfdi bjnullqah alri hvtqykyhs neyg syah elo zsvknl tpsija.","status":"draft","author":"name","display_time":"1979-04-28 12:25:49","pageviews":444},
			{"id":"430000197310143683","title":"Efyy tkdcf qtogo vflnf kmsmcdib fpgafx yvymoktv doxhpiomr gjcrkph mrvn rntvw nfb mlltzqf.","status":"draft","author":"name","display_time":"1991-10-23 05:33:36","pageviews":4817},
			{"id":"410000197912169836","title":"Lglxpt pxusiyvkjt rdkjjvrl busiy bifrcpzhp raykopcddn vgxja veikgpf isumdgya sjig cnnobibwc hvvhw eicu riuligb mkfzc ebvh tqydkh.","status":"deleted","author":"name","display_time":"2016-04-17 21:28:43","pageviews":2710},
			{"id":"520000198704186842","title":"Nhb zwaiyim vjfrgdrl hpsq cpjiius dvit olujbnh weog buwthorsl zxbmy hlqblwwtc npj jjvkbb xsymmylug qqxqvdt sgbgh.","status":"deleted","author":"name","display_time":"2005-01-27 09:49:57","pageviews":2283},
			{"id":"450000201510229660","title":"Grzjvyxvg tpyqxdi uihepwdu shyomonjhn pxskw lnyfxh ewpi hummsypr kbrp vdhlndbugc zcleuedd gbprqexes njgyh det vij ijc.","status":"draft","author":"name","display_time":"2004-06-06 09:53:25","pageviews":1729}
			]}})


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
	count = len(recordlist)
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
