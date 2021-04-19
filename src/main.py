import click
import os

from src.collector import pokemon
from src import create_app


def start():
    print('Poke trader started.')

    port = int(os.environ.get('PORT', 8000))
    prod = True if os.environ.get('HEROKU') == 'TRUE' else False
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=port,
        debug=not prod,
        use_reloader=not prod,
    )

@click.group(invoke_without_command=True)
@click.option('--start', is_flag=True, required=False,
              help='Start DB data.')
@click.option('--delete', is_flag=True, required=False,
              help='Delete DB data.')
def db_start(start, delete):
    print('Poke trader DB manager started.')
    if start:
        # collect all pokemon names and details
        pokemon.builder()
    elif delete:
        print('Delete not implemented yet.')