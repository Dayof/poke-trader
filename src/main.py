import os

import click

from src import create_app
from src.collector import pokemon


def check_envs():
    if not os.environ.get('MONGODB_PWD', False):
        return False
    return True


def start():
    print('Poke trader started.')

    if not check_envs():
        print('There are important environment variables that are not set, e.g.'
              ' MONGODB_PWD.')
        quit()

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
