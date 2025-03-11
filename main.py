from entities import pokemon, Pokemon, Player
from battletimer import Timer
from battle import Battle
from random import choice, randint
from utils import clear
from os import _exit
from utils import Status
from msvcrt import getch
import keystrokes

class Main():
    player: Player

    def main(self) -> int:
        # Ask for player's name and pokemon
        print("Welcome to Pokemon Red!")
        name = input("Please enter your name: ")

        print(f"Welcome {name}")
        print("Press 1 to start your journey or 2 to quit")
        match getch():
            case keystrokes.ONE:
                return self.start_journey(name)
            case _:
                return Status.QUIT

        # Start the battle
        match self.wild_pokemon():
            case Status.VICTORY:
                print("You won!")
            case Status.DEFEAT:
                print("You lost!")
            case Status.RUN_AWAY:
                print("You ran away!")
            case _:
                print("Invalid")
    
    def start_journey(self, name) -> int:
        try:
            selected_pokemon: Pokemon = pokemon[input("Choose your pokemon: ").capitalize()](0, 0)
        except KeyError:
            clear()
            print("Invalid pokemon")
            return Status.INVALID_POKEMON

        # Create player with the players name and selected pokemon
        self.player = Player(name, selected_pokemon)

        print(f"{name} you say goodbye to your mum and leave your small sleepy town behind! It's official you are now a pokemon trainer!")

        return Status.ERROR

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
    exit_code = Main().main()
    while exit_code != Status.SUCCESS and exit_code != Status.QUIT:
        exit_code = Main().main()
    
    if exit_code == Status.QUIT:
        print("Goodbye!")

    # Exit the program on completion
    _exit(0)