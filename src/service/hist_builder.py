from src.models import PokemonSchema


def build_players_lists(players_lists):
    new_players_lists = []
    pokemons = {}
    for plist_d in players_lists:
        player_1 = plist_d['pokemons_p1']
        player_2 = plist_d['pokemons_p2']
        new_players_list = {'player_1': [], 'player_2': []}
        for poke_id in player_1:
            if poke_id not in pokemons:
                pokemons[poke_id] = PokemonSchema.objects(key=poke_id).first()
            new_players_list['player_1'].append(pokemons[poke_id])
        for poke_id in player_2:
            if poke_id not in pokemons:
                pokemons[poke_id] = PokemonSchema.objects(key=poke_id).first()
            new_players_list['player_2'].append(pokemons[poke_id])
        new_players_lists.append(new_players_list)
    return new_players_lists
