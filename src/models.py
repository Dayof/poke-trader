from src import db_engine

class PokemonSchema(db_engine.Document):
    key = db_engine.IntField()
    name = db_engine.StringField()
    base_experience = db_engine.IntField()
    height = db_engine.IntField()
    weight = db_engine.IntField()
    types = db_engine.ListField(db_engine.StringField(), default=list)
    image_url = db_engine.URLField()
