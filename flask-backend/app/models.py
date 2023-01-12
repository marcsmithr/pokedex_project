from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type_id = db.Column(db.String(50), ForeignKey("pokemon_types.id"), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float(5, 2), default=1.00, nullable=False)
    catch_rate = db.Column(db.Float(5, 2), default=1.00, nullable=False)
    captured = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)


class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, ForeignKey("pokemons.id"))

class PokemonType(db.Model):
    __tablename__ = 'pokemon_types'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
