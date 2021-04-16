from src.models import PokemonSchema

import mongoengine as me
from tqdm import tqdm
import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'


def save_local(pokemon_details):
    me.connect(host='mongodb://127.0.0.1:27017/poketrader')
    pokemons_instances = [PokemonSchema(**data) for data in pokemon_details]
    PokemonSchema.objects.insert(pokemons_instances, load_bulk=False)

def builder():
    pokemon_names = get_all_names()  # ['name', 'url']
    pokemon_details = get_all_details(pokemon_names)
    save_local(pokemon_details)

def get_all_names():
    
    def len_pokemons():
        response = requests.get(BASE_URL)
        return response.json()['count']
    
    limit = len_pokemons()
    url = f'{BASE_URL}?limit={limit}'
    response = requests.get(url)
    return response.json()['results']

def get_all_details(pokemon_names):
    schema = ['name', 'base_experience', 'height', 'weight']
    all_pokemon_schema = []
    for pokemon in tqdm(pokemon_names):
        response = requests.get(pokemon['url'])
        details = response.json()
        poke_schema = {k: details[k] for k in schema }
        poke_schema['key'] = details['id']
        poke_schema['types'] = get_types(details['types'])
        poke_schema['image_url'] = get_sprite(details['sprites'])
        all_pokemon_schema.append(poke_schema)

    return all_pokemon_schema

def get_types(types):
    return [poke_type['type']['name'] for poke_type in types]

def get_sprite(sprites):
    return sprites['front_default']