#coding: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))
FLASK_CONFIG = 'default'
class Config():
    # DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    """
    sqllite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    PyMySQL   window 经常不好使
    pip.exe install PyMySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@1127.0.0.1:3306/support'

    pip.exe install PyMySQL
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/support'
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 6
    CSRF_ENABLED = True
    SECRET_KEY = 'Myadmin_secert'
    WTF_CSRF_SECRET_KEY = 'random key for form' # for csrf protection
    # Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', if you use the
    # bootstrap extension to create a form, it is Ok to use 'SECRET_KEY',
    # but when you use tha style like '{{ form.name.labey }}:{{ form.name() }}',
    # you must do this for yourself to use the wtf, more about this, you can
    # take a reference to the book <<Flask Framework Cookbook>>.
    # But the book only have the version of English.

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    ACAO_ACCESS_URL = 'http://127.0.0.1'

config = {
'development': DevConfig,
'production': ProdConfig,
'default': DevConfig
}