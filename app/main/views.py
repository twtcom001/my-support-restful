# coding:utf-8
import json
from flask import jsonify, abort, request 
from flask.ext.restful import Resource, fields, reqparse
from flask import render_template

from ..models import Permission, User, Logs, Plants, db, Account
from ..decorator import acao_auth
from . import main

#User 接口
@main.route('/', methods=['GET'])
#@acao_auth
def main_index():
	return render_template('index.html')