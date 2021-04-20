from flask import jsonify, render_template

from src.models import TradeSchema
from src.service import hist_builder

from . import history_api


@history_api.route('/history', methods=['GET'])
def get_history_menu():
    pokemons_lists = TradeSchema.objects()
    players_lists = hist_builder.build_players_lists(pokemons_lists)
    return render_template('history.html', detail=players_lists)
