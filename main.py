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

    action_dict = {
        # contains all possible action pairs, sorted.
        ("lizard", "lizard"): "The lizards are staring at each other lizardly.",
        ("lizard", "paper"): "The lizard devoured the paper!",
        ("lizard", "rock"): "This is how the dinosaurs went extinct.",
        ("lizard", "scissors"): "The scissors executed the lizard.",
        ("lizard", "Spock"): "The lizard was venomous and it bit Spock. Spock died.",
        ("paper", "paper"): "The papers combined and became a birthday card.",
        (
            "paper",
            "rock",
        ): "The paper covered the rock. The rock doesn't like being covered, apparently.",
        ("paper", "scissors"): "The paper is now two papers.",
        (
            "paper",
            "Spock",
        ): "The paper disproved Spock and gave him a paper cut. Spock is crying uncontrollably in the corner.",
        ("rock", "rock"): "We're stuck between a rock and a hard place.",
        (
            "rock",
            "scissors",
        ): "The scissors smashed themselves against the unbreakable rock.",
        ("rock", "Spock"): "Spock vaporized the rock. Seemed excessive.",
        ("scissors", "scissors"): "The scissors accepted an honorable draw.",
        ("scissors", "Spock"): "Spock destroyed the scissors because he could.",
        ("Spock", "Spock"): "Spock stopped looking at himself in the mirror.",
    }

    print("Testing.")
    return True


if __name__ == "__main__":
    while True:
        action = input()
        if not game_func(action):
            break
