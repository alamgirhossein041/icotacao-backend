from flask import Blueprint

bp = Blueprint('state', __name__)

from . import views

def init_app(app):
    app.register_blueprint(bp, url_prefix="/v1/admin/states")
