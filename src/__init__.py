# Examples of valid version strings
# 'X.Y.Z.devW'
# X: major modifications
# Y: minor modifications
# Z: bug fixes
# W: developmental release (build number)

__version__ = '0.0.1'


from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask import Flask


db_engine = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'poketrader',
        'host': 'localhost',
        'port': 27017
    }
    
    db_engine.init_app(app)

    from src.routers.general import general_api as general_api_blueprint
    app.register_blueprint(general_api_blueprint)

    from src.routers.pokemon import pokemon_api as pokemon_api_blueprint
    app.register_blueprint(pokemon_api_blueprint)

    CORS(app)

    return app
