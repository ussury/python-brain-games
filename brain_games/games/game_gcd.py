import math
import random


def rule():
    return 'Find the greatest common divisor of given numbers.'


def add_game_data():
    first_number = random.randint(1, 99)
    second_number = random.randint(1, 99)
    print(f'Question: {first_number} {second_number}')
    return math.gcd(first_number, second_number)
