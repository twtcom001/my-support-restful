from flask import Blueprint
v1_0 = Blueprint('v1_0', __name__)
from . import views