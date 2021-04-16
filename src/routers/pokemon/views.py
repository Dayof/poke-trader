from flask import render_template

from src.models import PokemonSchema
from . import pokemon_api


@pokemon_api.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemons = PokemonSchema.objects()
    return render_template('pokemon.html', pokemon_list=pokemons)
