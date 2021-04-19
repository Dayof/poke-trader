from flask import Blueprint

history_api = Blueprint('history_api', __name__)

from . import views