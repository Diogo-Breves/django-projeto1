from random import randint
from pprint import pprint

from faker import Faker


fake = Faker('pt_BR')


def rand_ratio():
    width = randint(840, 900)
    height = round(width * 9 / 16)

    return width, height


def make_cover():
    width, height = rand_ratio()
    random_id = randint(1, 999999)

    return {
        'url': (
            f'https://picsum.photos/seed/{random_id}/{width}/{height}'
        )
    }


def make_recipe():
    return {
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),

        'preparation_time': randint(10, 120),
        'preparation_time_unit': 'Minutos',

        'servings': randint(1, 10),
        'servings_unit': 'Porções',

        'preparation_steps': fake.text(max_nb_chars=3000),
        'created_at': fake.date_time(),

        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },

        'category': {
            'name': fake.word(),
        },

        'cover': make_cover(),
    }


if __name__ == '__main__':
    pprint(make_recipe())