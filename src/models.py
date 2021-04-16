from src import db_engine

class PokemonSchema(db_engine.Document):
    name = db_engine.StringField()
    url = db_engine.StringField()

    def to_json(self):
        return {'name': self.name, 'url': self.url}