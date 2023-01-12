from flask import Blueprint, render_template, redirect
from flask.json import jsonify
from ..forms import PokemonForm
from ..models import db, Pokemon, PokemonType, Item

pokemon_routes = Blueprint('pokemon', __name__)

@pokemon_routes.route('')
def pokemon():
    pokemons = Pokemon.query.all()
    return [pokemon.to_dict() for pokemon in pokemons]

@pokemon_routes.route('', methods=["POST"])
def post_pokemon():
    form = PokemonForm()
    pass
