from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    from app.models.customer_model import CustomerModel

    Migrate(app, app.db)
