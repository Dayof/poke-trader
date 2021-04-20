from src.models import PokemonSchema, TradeSchema


def is_trade_fair(points):
    return points <= 50


def get_score_by_id(list_player):
    exps = []
    for poke_id in list_player:
        cur_be = PokemonSchema.objects(key=poke_id).first()['base_experience']
        exps.append(cur_be)
    return exps


def get_experiences(list_player_1, list_player_2):
    total_player_1 = get_score_by_id(map(int, list_player_1))
    total_player_2 = get_score_by_id(map(int, list_player_2))
    return total_player_1, total_player_2


def manager_calc_base_exp(list_player_1, list_player_2):
    total_p1, total_p2 = get_experiences(list_player_1, list_player_2)
    return calc_base_experience(total_p1, total_p2)


def calc_base_experience(total_p1, total_p2):
    total_p1 = sum(total_p1)
    total_p2 = sum(total_p2)
    smallest_score = 1 if total_p2 >= total_p1 else 2
    diff_points = abs(total_p1 - total_p2)
    return {'smallest_score': smallest_score, 'diff_points': diff_points,
            'player_1': total_p1, 'player_2': total_p2}


def save_trade(list_player_1, list_player_2, base_exps):
    if is_trade_fair(base_exps['diff_points']):
        TradeSchema(pokemons_p1=list_player_1, pokemons_p2=list_player_2).save()
        return {**base_exps, 'status': 200}
    return {**base_exps, 'status': 500}
