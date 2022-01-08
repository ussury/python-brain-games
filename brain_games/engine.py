
def get_brain_games(rule):
    def get_user_name():
        return input('May I have your name? ')

    print('Welcome to the Brain Games!')
    user_name = get_user_name()
    print(f'Hello, {user_name}')
    print(rule())
    return user_name


def play(rule, add_game_data):
    user_name = get_brain_games(rule)

    def user_response():
        return input('Your answer: ')

    def play_iter(acc):
        if acc == 0:
            print(f'Congratulations, {user_name}!')
            return

        result = add_game_data()
        answer = user_response()

        if result == answer:
            print('Correct!')
            return play_iter(acc - 1)

        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {user_name}!")

    return play_iter(3)
