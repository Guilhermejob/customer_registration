from flask import Blueprint
from app.controllers.costumer import create, get_all_customers


bp_customer = Blueprint('bp_customer', __name__, url_prefix='/customer')

bp_customer.post('')(create)
bp_customer.get('')(get_all_customers)
