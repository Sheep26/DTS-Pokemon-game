from entities import pokemon, Pokemon, Player
from msvcrt import getch
from battletimer import Timer
from _thread import start_new_thread
from battle import Battle
from random import choice, randint

print("Press any key to start the game")
getch()

# Ask for player's name and pokemon
name = input("Enter your name: ")
selected_pokemon: Pokemon = pokemon[input("Choose your pokemon: ").capitalize()](0, 0)

if selected_pokemon == None:
    raise Exception("Invalid pokemon")

# Create player with the players name and selected pokemon
player = Player(name, selected_pokemon)

level: int = randint(0, 20)
exp: int = randint(0, int((1 * (0.25 * level)) * 100))

enemy = choice(list(pokemon.values()))(level, exp)
battle = Battle(player, enemy)

battle.start()