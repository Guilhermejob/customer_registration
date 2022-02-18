from flask import Flask
from app.routes.principal_blueprint import bp_principal
from app.routes.customer_blueprint import bp_customer
from app.routes.login_blueprint import bp_login
from flask_cors import CORS


def init_app(app: Flask):
    CORS(app)
    app.register_blueprint(bp_principal)
    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_login)
