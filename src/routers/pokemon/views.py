from flask import jsonify, render_template, request

from src.models import PokemonSchema
from src.service import calculator

from . import pokemon_api


@pokemon_api.route('/list/pokemon', methods=['GET'])
def get_pokemon_menu():
    pokemons = PokemonSchema.objects()[:200]
    return render_template('pokemon.html', pokemon_list=pokemons)


@pokemon_api.route('/pokemon/<poke_id>', methods=['GET'])
def get_pokemon(poke_id):
    pokemon = PokemonSchema.objects(key=poke_id).first()
    return jsonify({'results': render_template('pokedex.html',
                   detail=pokemon)})


@pokemon_api.route('/trade', methods=['POST'])
def trade_pokemon():
    body = request.json['data']
    p1, p2 = body[0], body[1]
    base_exps = calculator.manager_calc_base_exp(p1, p2)
    result = calculator.save_trade(p1, p2, base_exps)
    if result['status'] == 200:
        msg = {'msg': 'Successful trade!', **result}
    else:
        msg = {'msg': f'Trade is not fair. You need to add more '
                      f'{result["diff_points"]} points to player '
                      f'{result["smallest_score"]}', **result}
    return jsonify(msg), 200
