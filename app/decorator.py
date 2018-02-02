# coding:utf-8
import app 
from app import auth
from .models import Permission, User, Logs, Plants, db, Account
from flask import make_response, g, request, abort
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

@auth.verify_password
def verify_password(username_or_token, password):
    if request.path == "/api/v1.0/authtoken":
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    else:
        user = User.verify_auth_token(username_or_token)
        if not user:
            return False    
    g.user = user   
    return True

#验证token
def auth_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('X-Token')
        if token:
            g.current_user = User.verify_auth_token(token)
            if g.current_user:
                return f(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)
    return decorator  
