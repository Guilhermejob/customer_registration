from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.costumer_controllers import create, get_all_customers


bp_customer = Blueprint('bp_customer', __name__, url_prefix='/customer')

bp_customer.post('')(create)
bp_customer.get('')(jwt_required()(get_all_customers))
