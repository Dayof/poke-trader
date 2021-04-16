import click
import os

from src.collector import pokemon
from src import create_app


def start():
    print('Poke trader started.')

    port = int(os.environ.get('PORT', 8000))
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        use_reloader=True,
    )

@click.group(invoke_without_command=True)
@click.option('--start', is_flag=True, required=False,
              help='Start DB data.')
@click.option('--delete', is_flag=True, required=False,
              help='Delete DB data.')
def db_start(start, delete):
    print('Poke trader DB manager started.')
    if start:
        # collect all pokemon names
        pokemons = pokemon.get_all()
        pokemon.save_local(pokemons)
    elif delete:
        print('Delete not implemented yet.')