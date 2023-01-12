from flask import Blueprint, render_template, redirect
from ..forms import PokemonForm
from ..models import db, Pokemon, PokemonType, Item

pokemon_routes = Blueprint('pokemon', __name__)

@pokemon_routes.route('')
def pokemon():
    pokemons = Pokemon.query.all()
    return {pokemon.id: pokemon for pokemon in pokemons}
