from entities import pokemon, Pokemon, Player
from battletimer import Timer
from battle import Battle
from random import choice, randint
from utils import clear
from os import _exit

class Main():
    player: Player

    def main(self) -> int:
        # Ask for player's name and pokemon
        name = input("Enter your name: ")
        try:
            selected_pokemon: Pokemon = pokemon[input("Choose your pokemon: ").capitalize()](0, 0)
        except KeyError:
            print("Invalid pokemon")
            return 1

        # Create player with the players name and selected pokemon
        self.player = Player(name, selected_pokemon)

        # Start the battle
        match self.wild_pokemon():
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

    def wild_pokemon(self) -> int:
        # Pick random values for the level and exp
        level: int = randint(0, 5)
        exp: int = randint(0, int((1 * (0.25 * level)) * 100))

        # Create a random enemy instance
        enemy = choice(list(pokemon.values()))(level, exp)

        # Create a battle instance
        battle = Battle(self.player, enemy)

        # Clear the console
        clear()

        return battle.start()

if __name__ == "__main__":
    # We're not using __init__ here because we want to return a value from the main function
    # If the main function wasn't successful try again
    while Main().main() != 0:
        continue

    # Exit the program on completion
    _exit(0)