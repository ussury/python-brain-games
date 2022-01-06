import random


def rule():
    return 'What is the result of the expression?'


def result_expression(first_number, second_number, simbol):
    operations = {
        '+': str(first_number + second_number),
        '-': str(first_number - second_number),
        '*': str(first_number * second_number),
    }
    return operations[simbol]


def get_operator():
    def operator(coll):
        return random.choice(coll)

    operators_coll = ['+', '-', '*']

    return operator(operators_coll)


def add_game_data():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 10)
    operator = get_operator()
    print(f'Question: {first_number} {operator} {second_number}')
    return result_expression(first_number, second_number, operator)
