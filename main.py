from entities import pokemon, Pokemon, Player
from msvcrt import getch
from battletimer import Timer
from _thread import start_new_thread

print("Press any key to start the game")
getch()

# Ask for player's name and pokemon
name = input("Enter your name: ")
pokemon: Pokemon = pokemon[input("Choose your pokemon: ").capitalize()](0, 0)

# Create player with the players name and selected pokemon
player = Player(name, pokemon)

# Main game loop
while-True:
    pass