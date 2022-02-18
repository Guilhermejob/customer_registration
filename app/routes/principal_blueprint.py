from flask import Blueprint


from app.controllers.welcome import welcome

bp_principal = Blueprint('bp_clients', __name__, url_prefix='/')

bp_principal.get('')(welcome)
