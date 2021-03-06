#coding: utf-8
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app, g
from . import db




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    nickname = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))
    head_img = db.Column(db.String(200))
    is_valid = db.Column(db.Boolean, default=True)
    last_login = db.Column(db.DateTime, doc="最后登录时间")
    
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    @staticmethod
    def insert_admin(username, nickname, password, role_id):
        user = User(username=username, nickname=nickname, password=password, role_id=role_id)
        db.session.add(user)
        db.session.commit()


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.username is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(
                    self.username.encode('utf-8')).hexdigest()

    def gravatar(self, size=40, default='identicon', rating='g'):
        # if request.is_secure:
        #     url = 'https://secure.gravatar.com/avatar'
        # else:
        #     url = 'http://www.gravatar.com/avatar'
        url = 'http://gravatar.duoshuo.com/avatar'
        hash = self.avatar_hash or hashlib.md5(
            self.username.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)
 
    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def generate_auth_token(self, expiration = 7200):
        s = Serializer(current_app.config.get('SECRET_KEY'), expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(uername_or_token):
        s = Serializer(current_app.config.get('SECRET_KEY'))
        try:
            data = s.loads(uername_or_token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user


class AnonymousUser(AnonymousUserMixin):
    def can(slef, permissions):
        return False

    def is_administrator(self):
        return False

class Permission:
    ADMINISTER = 0x01
    LOGIN = 0x02

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.LOGIN, True),
            'Admin': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
                role.permissions = roles[r][0]
                role.default = roles[r][1]
                db.session.add(role)
            db.session.commit()

class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    level = db.Column(db.Integer)
    op_time = db.Column(db.DateTime, doc="最后登录时间")
    comment = db.Column(db.String(255)) 

    
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(20))
    date = db.Column(db.Date, doc="录入时间")
    total = db.Column(db.Float)
    src = db.Column(db.String(20))
    comment = db.Column(db.String(255), doc="备注")

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.String(64), unique=True, doc="编号")
    osn = db.Column(db.String(64), doc="旧编号")
    familia = db.Column(db.String(64), default='cactus', doc="科")
    genus = db.Column(db.String(40), doc="属")
    icbn_name = db.Column(db.String(255), doc="拉丁名")
    chinese_name = db.Column(db.String(100), doc="中文名")
    summary = db.Column(db.String(255), doc="简介")

class Dict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    father = db.Column(db.String(255), doc="父节点")
    key = db.Column(db.String(255), doc="键")
    value = db.Column(db.String(255), doc="值")


class Introduce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    producer_name = db.Column(db.String(255), doc="生产商")
    introduce_type = db.Column(db.String(255), doc="引进类型")
    price = db.Column(db.Float, doc="引进价格")
    date = db.Column(db.Date, doc="引进时间")
    count = db.Column(db.Integer, doc="数量")
    comment = db.Column(db.String(255), doc="备注")

class Reproduce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plants_id = db.Column(db.Integer, db.ForeignKey('plants.id'))
    reproduce_type = db.Column(db.String(255), doc="繁殖类型")
    date = db.Column(db.Date, doc="时间")
    count = db.Column(db.Integer, doc="数量")
    comment = db.Column(db.String(255), doc="备注")

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), doc="姓名")
    address = db.Column(db.String(255), doc="地址")
    address_type = db.Column(db.String(255), doc="地址类型")
    mobile = db.Column(db.String(15), doc="手机号")
    telephone = db.Column(db.String(15), doc="电话")
    comment = db.Column(db.String(255), doc="备注")


