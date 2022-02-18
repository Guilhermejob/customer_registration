from flask import Flask
from os import getenv
from app import routes
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    routes.init_app(app)

    return app
