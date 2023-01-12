from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class PokemonForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    attack = IntegerField('Attack', validators=[DataRequired()])
    defense = IntegerField('Defense', validators=[DataRequired()])
    image_url = StringField('Image Url', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices=["fire", "electric", "normal", "ghost", "psychic", "water", "bug", "dragon", "grass", "fighting", "ice", "flying", "poison", "ground", "rock", "steel"], validators=[DataRequired()])
    moves = StringField('Moves', validators=[DataRequired()])
    encounter_rate = FloatField('Encounter Rate', validators=[DataRequired()])
    catch_rate = FloatField('Catch Rate', validators=[DataRequired()])
    captured = BooleanField('Captured', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Items(FlaskForm):
    happiness = IntegerField('Happiness', validators=[DataRequired()])
    image_url = StringField('Image Url', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
