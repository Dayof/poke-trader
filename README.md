<p align="center">
  <img src="src/static/image/poke.png"
			width="100px"/>
  <h4 align="center">Poke Trader</h4>
  <p align="center">
    <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg"/>
  </p>
</p>

Poke Trader
------------

Este projeto consiste em uma calculadora de trocas de pokemon.
É possível utilizar esta ferramenta tanto por APIs ou via UI.

Todos os dados dos pokemons foram coletados através do serviço ​https://pokeapi.co/docs/v2.

## Requisitos do sistema

- Python 3.7+
- MongoDB 3.6.8+

## Uso do sistema

```
python3 -m venv venv
. venv/bin/activate
pip install -U pip
pip install -e .[dev]
```