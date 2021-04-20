import os

import click

from src import create_app
from src.collector import pokemon


def check_envs():
    """Checks environment variables.

    The MONGODB_PWD is a needed variable to enable mongodb connection.

    Returns:
        bool: If all needed environment variables are set.
    """
    if not os.environ.get('MONGODB_PWD', False):
        return False
    return True


def start():
    """Start APP.

    Flask server details: host 0.0.0.0 and default port 8000.
    The HEROKU variable is used to allow the app to switch between
    production and develop environment.
    """
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
    """Start Poke Trader DB manager.

    Starts Poke Trader database manager.

    Args:
        start (bool): Flag to starts database creation.
        delete (bool): Flag to starts database removal.
    """
    print('Poke trader DB manager started.')
    if start:
        # collect all pokemon names and details
        pokemon.builder()
    elif delete:
        print('Delete not implemented yet.')
