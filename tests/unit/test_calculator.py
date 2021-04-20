import pytest

from src.service import calculator


def test_successful_trade():
    pokemon_p1, pokemon_p2 = [20, 30], [40, 20]
    base_exps = calculator.calc_base_experience(pokemon_p1, pokemon_p2)
    assert calculator.is_trade_fair(base_exps['diff_points'])


def test_failure_trade():
    pokemon_p1, pokemon_p2 = [20, 30], [101]
    base_exps = calculator.calc_base_experience(pokemon_p1, pokemon_p2)
    assert not calculator.is_trade_fair(base_exps['diff_points'])
