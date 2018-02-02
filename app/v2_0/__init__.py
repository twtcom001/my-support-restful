from flask import Blueprint
v2_0 = Blueprint('v2_0', __name__)
from . import views