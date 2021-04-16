from flask import render_template, jsonify

from src.models import PokemonSchema
from . import pokemon_api


@pokemon_api.route('/list/pokemon', methods=['GET'])
def get_pokemon_list():
    pokemons = PokemonSchema.objects()[:20]
    return render_template('pokemon.html', pokemon_list=pokemons)

@pokemon_api.route('/pokemon/<poke_id>', methods=['GET'])
def get_pokemon(poke_id):
    pokemon = PokemonSchema.objects(key=poke_id).first()
    return jsonify({'results': render_template('pokedex.html', detail=pokemon)})

