from entities import pokemon, Pokemon, Player
from msvcrt import getch
from battletimer import Timer
from battle import Battle
from random import choice, randint
from utils import clear
from os import _exit

def main() -> int:
    # Ask for player's name and pokemon
    name = input("Enter your name: ")
    try:
        selected_pokemon: Pokemon = pokemon[input("Choose your pokemon: ").capitalize()](0, 0)
    except KeyError:
        print("Invalid pokemon")
        return 1

    # Create player with the players name and selected pokemon
    player = Player(name, selected_pokemon)

    # Pick random values for the level and exp
    level: int = randint(0, 5)
    exp: int = randint(0, int((1 * (0.25 * level)) * 100))

    # Create a random enemy instance
    enemy = choice(list(pokemon.values()))(level, exp)

    # Create a battle instance
    battle = Battle(player, enemy)

    # Clear the console
    clear()

    # Start the battle
    match battle.start():
        case 0:
            print("You won!")
        case 1:
            print("You lost!")
        case 2:
            print("You ran away!")
        case _:
            print("Invalid input")

            return 2

    return 0

def run():
    exit_code = main()
    if exit_code == 1:
        # Recursion? could cause memory issues if handled incorrectly.
        run()
    else:
        _exit(exit_code)

if __name__ == "__main__":
    run()