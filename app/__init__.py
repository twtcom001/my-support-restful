#coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

from config import config

db = SQLAlchemy()

auth = HTTPBasicAuth()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #old front
    from .v1_0 import v1_0 as v1_0_blueprint
    app.register_blueprint(v1_0_blueprint, url_prefix='/api/v1.0')
    #new front
    from .v2_0 import v2_0 as v2_0_blueprint
    app.register_blueprint(v2_0_blueprint, url_prefix='/api/v2.0')
    # 植物相关接口
    from .v2_1 import v2_1 as v2_1_blueprint
    app.register_blueprint(v2_1_blueprint, url_prefix='/api/v2.1')

    return app

