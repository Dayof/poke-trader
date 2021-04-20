from flask import Blueprint

general_api = Blueprint('general_api', __name__)

from . import views
