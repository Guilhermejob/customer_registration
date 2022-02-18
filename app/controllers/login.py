from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.models.customer_model import CustomerModel
