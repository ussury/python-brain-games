import random


def rule():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_prime_num(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def add_game_data():
    random_number = random.randint(2, 99)
    print(f'Question: {random_number}')
    return calculate_prime_num(random_number)
