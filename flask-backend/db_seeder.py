from app.models import db, Pokemon, Items
from app import app
from random import randint

with app.app_context():

    db.drop_all()
    db.create_all()

    all_pokemon = [Pokemon(
        number=1,
        image_url='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves=[
            'tackle',
            'vine whip'
        ],
        captured=True
    ), Pokemon(
        number=2,
        image_url='/images/pokemon_snaps/2.svg',
        name='Ivysaur',
        attack=62,
        defense=63,
        type='grass',
        moves=[
            'tackle',
            'vine whip',
            'razor leaf'
        ],
        captured=True
    ), Pokemon(
        number=3,
        image_url='/images/pokemon_snaps/3.svg',
        name='Venusaur',
        attack=82,
        defense=83,
        type='grass',
        moves=[
            'tackle',
            'vine whip',
            'razor leaf'
        ],
        captured=True
    ), Pokemon(
        number=4,
        image_url='/images/pokemon_snaps/4.svg',
        name='Charmander',
        attack=52,
        defense=43,
        type='fire',
        moves=[
            'scratch',
            'ember',
            'metal claw'
        ],
        captured=True
    ), Pokemon(
        number=5,
        image_url='/images/pokemon_snaps/5.svg',
        name='Charmeleon',
        attack=64,
        defense=58,
        type='fire',
        moves=[
            'scratch',
            'ember',
            'metal claw',
            'flamethrower'
        ],
        captured=True
    ), Pokemon(
        number=6,
        image_url='/images/pokemon_snaps/6.svg',
        name='Charizard',
        attack=84,
        defense=78,
        type='fire',
        moves=[
            'flamethrower',
            'wing attack',
            'slash',
            'metal claw'
        ],
        captured=True
    ), Pokemon(
        number=7,
        image_url='/images/pokemon_snaps/7.svg',
        name='Squirtle',
        attack=48,
        defense=65,
        type='water',
        moves=[
            'tackle',
            'bubble',
            'water gun'
        ],
        captured=True
    ), Pokemon(
        number=8,
        image_url='/images/pokemon_snaps/8.svg',
        name='Wartortle',
        attack=63,
        defense=80,
        type='water',
        moves=[
            'tackle',
            'bubble',
            'water gun',
            'bite'
        ],
        captured=True
    ), Pokemon(
        number=9,
        image_url='/images/pokemon_snaps/34.svg',
        name='Nidoking',
        attack=92,
        defense=77,
        type='poison',
        moves=[
            'peck',
            'poison sting',
            'megahorn'
        ],
    ), Pokemon(
        number=10,
        image_url='/images/pokemon_snaps/17.svg',
        name='Pidgeotto',
        attack=60,
        defense=55,
        type='normal',
        moves=[
            'tackle',
            'gust',
            'wing attack'
        ]
    ), Pokemon(
        number=11,
        image_url='/images/pokemon_snaps/9.svg',
        name='Blastoise',
        attack=83,
        defense=100,
        type='water',
        moves=[
            'hydro pump',
            'bubble',
            'water gun',
            'bite'
        ]
    ), Pokemon(
        number=12,
        image_url='/images/pokemon_snaps/10.svg',
        name='Caterpie',
        attack=30,
        defense=35,
        type='bug',
        moves=[
            'tackle'
        ]
    ), Pokemon(
        number=13,
        image_url='/images/pokemon_snaps/12.svg',
        name='Butterfree',
        attack=45,
        defense=50,
        type='bug',
        moves=[
            'confusion',
            'gust',
            'psybeam',
            'silver wind'
        ]
    ), Pokemon(
        number=14,
        image_url='/images/pokemon_snaps/13.svg',
        name='Weedle',
        attack=35,
        defense=30,
        type='bug',
        moves=[
            'poison sting'
        ]
    ), Pokemon(
        number=15,
        image_url='/images/pokemon_snaps/16.svg',
        name='Pidgey',
        attack=45,
        defense=40,
        type='normal',
        moves=[
            'tackle',
            'gust'
        ]
    ),]

    add_pokemon = [db.session.add(pokemon) for pokemon in all_pokemon]
    db.session.commit()

    def random_image():
        images = [
            "/images/pokemon_berry.svg",
            "/images/pokemon_egg.svg",
            "/images/pokemon_potion.svg",
            "/images/pokemon_super_potion.svg",
        ]

        index = randint(0, len(images))
        return images[index]

    def generate_items():
        item_list = []
        item_name_list = [
            "apricot berry",
            "big mushroom",
            "burn heal",
            "float stone",
            "mago berry",
            "pearl"
        ]
        
        for pokemon in all_pokemon:
            for i in range(2):
                item = Items(
                 pokemon.id,
                 happiness=randint(1, 100),
                 price=randint(1, 100),
                 image_url=random_image(),
                 name=item_name_list[randint(0, len(item_name_list)-1)]
                )

                item_list.append(item)
        print(item_list)    