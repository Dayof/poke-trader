from flask import Blueprint

pokemon_api = Blueprint('pokemon_api', __name__)

from . import views
