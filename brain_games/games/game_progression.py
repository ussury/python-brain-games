import random


def rule():
    return 'What number is missing in the progression?'


def get_progression_list():
    """ создаем список числовой прогрессии """
    coll = []
    value = random.randint(1, 5)
    step = random.randint(1, 4)
    count = 1

    while count < 11:
        coll.append(str(value))
        value += step
        count += 1

    return coll


def console_list(coll, random_num):
    """ вывод числовой прогрессии с пропущенным числом в консоль """
    new_coll = []
    space = '..'
    for i in range(len(coll)):
        if coll[i] == random_num:
            coll[i] = space
        new_coll.append(coll[i])

    return ' '.join(new_coll)


def add_game_data():
    progress_coll = get_progression_list()
    result = random.choice(progress_coll)
    result_coll = console_list(progress_coll, result)
    print(f'Question: {result_coll}')
    return result
