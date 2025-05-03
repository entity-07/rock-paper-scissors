
import random
from enum import Enum


class Opponent:
    class Choice(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def __init__(self):
        self.choice = random.choice(list(Opponent.Choice))


class Player:
    class Choice(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        NONE = 4

    def __init__(self, choice):
        self.choice = choice


def compare_guess(player_choice, opponent_choice):
    if player_choice == Player.Choice.ROCK:
        if opponent_choice == Opponent.Choice.PAPER:
            return "You lose"
        elif opponent_choice == Opponent.Choice.SCISSORS:
            return "You win"
        elif opponent_choice == Opponent.Choice.ROCK:
            return "It's a draw"

    elif player_choice == Player.Choice.PAPER:
        if opponent_choice == Opponent.Choice.SCISSORS:
            return "You lose"
        elif opponent_choice == Opponent.Choice.ROCK:
            return "You win"
        elif opponent_choice == Opponent.Choice.PAPER:
            return "It's a draw"

    elif player_choice == Player.Choice.SCISSORS:
        if opponent_choice == Opponent.Choice.ROCK:
            return "You lose"
        elif opponent_choice == Opponent.Choice.PAPER:
            return "You win"
        elif opponent_choice == Opponent.Choice.SCISSORS:
            return "It's a draw"

    return "Invalid choice"
