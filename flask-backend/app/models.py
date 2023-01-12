from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey
from datetime import datetime

db = SQLAlchemy()

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type_id = db.Column(db.Integer, ForeignKey("pokemon_types.id"), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float(5, 2), default=1.00, nullable=False)
    catch_rate = db.Column(db.Float(5, 2), default=1.00, nullable=False)
    captured = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.Date, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.Date, default=datetime.now(), nullable=False)

    types = db.relationship("PokemonType", back_populates='pokemon')
    items = db.relationship("Item", back_populates='pokemon', cascade="all, delete")
    # moves = db.relationship("Move", back_populates='pokemon', cascade="all, delete")

    def to_dict(self):
        # print('pokemon', self.name, '------- types', self.types.type)
        # return 'no'
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageUrl": self.image_url,
            "name": self.name,
            "type": self.types.type, #this might need to be changed to type_id
            "moves": self.moves,
            "encounterRate": self.encounter_rate,
            "catchRate": self.catch_rate,
            "captured": self.captured,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }

# class Move(db.Model):
#     __tablename__ = 'moves'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)

#     pokemon = db.relationship("Pokemon", back_populates='moves')

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name
#         }

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, ForeignKey("pokemons.id"))

    pokemon = db.relationship("Pokemon", back_populates='items')

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "imageUrl": self.image_url,
            "name": self.name,
            "price": self.price,
            "pokemon": self.pokemon #same with type_id
        }

class PokemonType(db.Model):
    __tablename__ = 'pokemon_types'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)

    pokemon = db.relationship("Pokemon", back_populates="types", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }
