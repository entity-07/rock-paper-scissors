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

    def __init__(self, choice):
        self.choice = choice


def get_user_input():
    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSORS")

    user_input = input(
        "What hand are you gonna play(chose a number from 1-3): ")

    try:
        choice_number = int(user_input)
        if choice_number in [choice.value for choice in Player.Choice]:
            user_choice = Player.Choice(choice_number)
            return user_choice
        else:
            print("Invalid. Pick either 1, 2 or 3: ")
            return None
    except ValueError:
        print("Invalid. Pick a number: ")
        return None


player_choice = get_user_input()
print(player_choice)
#
opponent_choice = Opponent()
print("The opponent chose " + str(opponent_choice.choice.name))


def compare_guess():
    if player_choice == Player.Choice.ROCK:
        if opponent_choice.choice == Opponent.Choice.PAPER:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you lose")

        elif opponent_choice.choice == Opponent.Choice.SCISSORS:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you win")

        elif opponent_choice.choice == Opponent.Choice.ROCK:
            print("The opponent chose: " +
                  str(opponent_choice.choice) + ", it's a draw")

    elif player_choice == Player.Choice.PAPER:
        if opponent_choice.choice == Opponent.Choice.SCISSORS:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you lose")

        elif opponent_choice.choice == Opponent.Choice.ROCK:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you win")

        elif opponent_choice.choice == Opponent.Choice.PAPER:
            print("The opponent chose: " +
                  str(opponent_choice.choice) + ", it's a draw")

    elif player_choice == Player.Choice.SCISSORS:
        if opponent_choice.choice == Opponent.Choice.ROCK:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you lose")

        elif opponent_choice.choice == Opponent.Choice.PAPER:
            print("The opponent chose " +
                  str(opponent_choice.choice) + ", you win")

        elif opponent_choice.choice == Opponent.Choice.SCISSORS:
            print("The opponent chose: " +
                  str(opponent_choice.choice) + ", it's a draw")


compare_guess()
