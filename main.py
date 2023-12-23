"""
Basic rock-paper-scissors-lizard-Spock game.
"""

import random


def game_func(action: str) -> bool:
    """
    Function that plays a single game.
    Takes user action as input (e.g. "rock"), randomly generates computer
    action, and prints output accordingly.
    """
    if action == "exit":
        print("I see that you have accepted defeat!")
        return False

    print("Testing.")
    return True


if __name__ == "__main__":
    while True:
        action = input()
        if not game_func(action):
            break
