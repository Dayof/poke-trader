from src.models import PokemonSchema, TradeSchema

def is_trade_fair(points):
    return points <= 50

def get_score_by_id(list_player):
    exps = []
    for poke_id in list_player:
        exps.append(PokemonSchema.objects(key=poke_id).first()['base_experience'])
    return exps

def calc_base_experience(list_player_1, list_player_2):
    total_player_1 = sum(get_score_by_id(map(int, list_player_1)))
    total_player_2 = sum(get_score_by_id(map(int, list_player_2)))
    smallest_score = 1 if total_player_2 >= total_player_1 else 2
    diff_points = abs(total_player_1 - total_player_2)
    return {'smallest_score': smallest_score, 'diff_points': diff_points,
            'player_1': total_player_1, 'player_2': total_player_2}

def save_trade(list_player_1, list_player_2):
    result = calc_base_experience(list_player_1, list_player_2)
    if is_trade_fair(result['diff_points']):
        TradeSchema(pokemons_p1=list_player_1, pokemons_p2=list_player_2).save()
        return {**result, 'status': 200}
    return {**result, 'status': 500}
