from flask import Blueprint, render_template, redirect, request
from flask.json import jsonify
# from flask_cors import cross_origin
from ..forms import PokemonForm
from ..models import db, Pokemon, PokemonType, Item

pokemon_routes = Blueprint('pokemon', __name__, url_prefix='/api/pokemon')

@pokemon_routes.route('')
# @cross_origin()
def pokemon():
    pokemons = Pokemon.query.all()
    poke_list = [pokemon.to_dict() for pokemon in pokemons]
    # print('pokemon ------------------', [pokemon.to_dict() for pokemon in pokemons])
    return poke_list

@pokemon_routes.route('', methods=["POST"])
# @cross_origin()
def post_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_pokemon = Pokemon()
        form.populate_obj(new_pokemon)

        db.session.add(new_pokemon)
        db.session.commit()

        return redirect(f'/{new_pokemon.id}')

    if form.errors:
        print(form.errors)

    return redirect('')

@pokemon_routes.route('/<int:id>')
def single(id):
    pokemon = Pokemon.query.get(id)

    poke = pokemon.to_dict()

    poke['moves'] = poke['moves'].split(', ')

    print(poke['moves'])

    return poke
