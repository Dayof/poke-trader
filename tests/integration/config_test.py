import pytest
from src import create_app
from flask import g


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app('test')
    client = flask_app.test_client()
    context = flask_app.app_context()
    context.push()

    yield client

    context.pop()
