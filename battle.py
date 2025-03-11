from entities import Player, Pokemon
from battletimer import Timer
from msvcrt import getch
from utils import clear
# I would import all from keystrokes.py as "from keystrokes import *" for good practice,
# But it was causing some issues with built-in python functions.
import keystrokes

class Battle:
    player: Player
    enemy: Pokemon

    def __init__(self, player: Player, enemy: Pokemon):
        self.player = player
        self.enemy = enemy

    def start(self) -> int:
        # Tell the user that a wild pokemon appeared
        print(f"A wild {self.enemy.get_name()} appeared!")
        print(f"It's a {self.enemy.get_type_name()} type!")
        print(f"Level: {self.enemy.level}")
        print(f"HP: {self.enemy.hp}/{self.enemy.max_hp}")

        # Ask the user if they want to fight or run
        print("--------------------")
        print("1. Fight")
        print("2. Run")
        print("--------------------")

        # Get user input, getch() returns a byte so we need to compare it to a byte
        match getch():
            case keystrokes.ONE:
                return self.battle()
            case _:
                return 2
    
    def battle(self) -> int:
        print(f"You choose to fight with {self.player.get_pokemon().get_name()}!")

        # Start the countdown timer before the battle
        Timer(3).countdown()
        print("Go!")

        player_turn = True

        while-True:
            clear()
            # It's the players turn to attack
            if player_turn:
                # Print the player's pokemon's name and HP
                print(f"Player Pokemon: {self.player.pokemon.get_name()}")
                print(f"HP: {self.player.pokemon.get_hp()}/{self.player.pokemon.get_max_hp()}")
                # Print the enemy's name and HP
                print(f"Enemy Pokemon: {self.enemy.get_name()}")
                print(f"HP: {self.enemy.get_hp()}/{self.enemy.get_max_hp()}\n")

                # Ask the player to pick an attack
                print("Pick an attack:")
                print("--------------------")

                # Cycle through the player's pokemon's attacks and print them out
                count = 1
                for attack in self.player.pokemon.attacks:
                    print(f"{count}: {attack.name} - {attack.damage} dmg - {attack.accuracy}% accuracy")
                    count += 1
                print("--------------------")

                try:
                    # Get the attack the player wants to use from the list of attacks that the player's pokemon has
                    attack = self.player.pokemon.attacks[int(getch()) - 1]

                    # Attack the target enemy with the selected attack and check if it was successful
                    if self.player.get_pokemon().attack(self.enemy, attack):
                        print("Attack successful!")
                        print(f"{self.enemy.get_name()} HP: {self.enemy.get_hp()}/{self.enemy.get_max_hp()}")
                    else:
                        print("You missed!")
                    
                    player_turn = False
                # If there is a value error or index error, the player entered an invalid attack
                except (ValueError, IndexError):
                    print("Invalid attack")
            else:
                # It's the enemy's turn to attack
                print(f"{self.enemy.get_name()}'s turn")

                # Pick a random attack from the enemy's list of attacks
                attack = self.enemy.pick_attack()

                print(f"{self.enemy.get_name()} chooses {attack.name}!")

                # Attack the player with the selected attack and check if it was successful
                if self.enemy.attack(self.player.pokemon, attack):
                    print("Attack successful!")
                    print(f"{self.player.pokemon.get_name()} HP: {self.player.pokemon.get_hp()}/{self.player.pokemon.get_max_hp()}")
                else:
                    print(f"{self.enemy.get_name()} missed!")
                
                player_turn = True
        return 0