from flask import Flask
from app.routes.principal_blueprint import bp_principal


def init_app(app: Flask):
    app.register_blueprint(bp_principal)
