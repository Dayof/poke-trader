from src.models import PokemonSchema

import mongoengine as me
import requests

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'


def save_local(pokemons):
    me.connect(host='mongodb://127.0.0.1:27017/poketrader')
    pokemons_instances = [PokemonSchema(**data) for data in pokemons]
    PokemonSchema.objects.insert(pokemons_instances, load_bulk=False)


def get_all():
    limit = len_pokemons()
    url = f'{BASE_URL}?limit={limit}'
    response = requests.get(url)
    return response.json()['results']


def len_pokemons():
    response = requests.get(BASE_URL)
    return response.json()['count']