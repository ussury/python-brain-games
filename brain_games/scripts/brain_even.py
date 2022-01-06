#!/usr/bin/env python3

from brain_games.engine import play
from brain_games.games.game_even import rule, add_game_data


def main():
    return play(rule, add_game_data)


if __name__ == '__main__':
    main()
