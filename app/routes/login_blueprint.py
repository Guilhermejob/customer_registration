from flask import Blueprint
from app.controllers.login_controllers import signin_customer

bp_login = Blueprint("bp_login", __name__, url_prefix='/login')


bp_login.post('')(signin_customer)
