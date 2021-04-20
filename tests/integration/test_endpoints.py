import pytest
import json
import mongoengine as me
from config_test import test_client


def test_home_200(test_client):
    assert test_client.get('/').status_code == 200


def test_history_200(test_client):
    assert test_client.get('/history').status_code == 200


def test_list_pokemons_200(test_client):
    assert test_client.get('/list/pokemon').status_code == 200
