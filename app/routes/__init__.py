from flask import Flask
from app.routes.principal_blueprint import bp_principal
from app.routes.customer_blueprint import bp_customer


def init_app(app: Flask):
    app.register_blueprint(bp_principal)
    app.register_blueprint(bp_customer)
