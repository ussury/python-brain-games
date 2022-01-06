import random


def rule():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def add_game_data():
    value = random.randint(1, 99)
    print(f'Question: {value}')
    return 'yes' if value % 2 == 0 else 'no'
