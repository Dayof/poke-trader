# Examples of valid version strings
# 'X.Y.Z.devW'
# X: major modifications
# Y: minor modifications
# Z: bug fixes
# W: developmental release (build number)

__version__ = '1.2.0'


import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

db_engine = MongoEngine()


def create_app(mode='app'):
    """Create Flask app.

    This function starts Flask, with its routers, and MongoDB host settings.

    Returns:
        app (:obj:`Flask`) Flask object reference.
    """
    app = Flask(__name__)
    if mode == 'app':
        mongodb_pwd = os.environ.get('MONGODB_PWD')
        mongodb = f'mongodb+srv://bxblue:{mongodb_pwd}@cluster0.fk2ly' \
                '.mongodb.net/poketrader?retryWrites=true&w=majority'
    else:
        mongodb = 'mongodb://localhost:27017'

    app.config['MONGODB_SETTINGS'] = {
        'host': mongodb
    }

    db_engine.init_app(app)

    from src.routers.general import general_api as general_api_blueprint
    app.register_blueprint(general_api_blueprint)

    from src.routers.pokemon import pokemon_api as pokemon_api_blueprint
    app.register_blueprint(pokemon_api_blueprint)

    from src.routers.history import history_api as history_api_blueprint
    app.register_blueprint(history_api_blueprint)

    CORS(app)

    return app
