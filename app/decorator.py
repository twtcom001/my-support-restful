# coding:utf-8
import app 

from flask import make_response 
from functools import wraps
from config import  config, FLASK_CONFIG

#验证跨域ACAO 认证
def acao_auth(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		response = make_response(f(*args, **kwargs))  
		# Access-Control-Allow-Origin 访问URL
		response.headers['Access-Control-Allow-Origin'] = config[FLASK_CONFIG].ACAO_ACCESS_URL
		response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
		response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
		return response
	return wrapper