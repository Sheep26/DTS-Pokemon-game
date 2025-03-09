from entities import Player, Pokemon
from battletimer import Timer
from msvcrt import getch

class Battle:
    player: Player
    enemy: Pokemon

    def __init__(self, player: Player, enemy: Pokemon):
        self.player = player
        self.enemy = enemy

    def start(self) -> int:
        print(f"A wild {self.enemy.get_name()} appeared!")
        print(f"It's a {self.enemy.get_type_name()} type!")
        print(f"Level: {self.enemy.level}")
        print(f"HP: {self.enemy.get_hp()}/{self.enemy.get_max_hp()}")

        print("--------------------")
        print("1. Fight")
        print("2. Run")
        print("--------------------")

        match getch():
            case b'1':
                return self.battle()
            case _:
                return 2
    
    def battle(self) -> int:
        Timer(3).countdown()
        print("Go!")

        print(f"You choose to fight with {self.player.pokemon.get_name()}!")

        player_turn = True

        while-True:
            if player_turn:
                print("Pick an attack:")
                print("--------------------")
                count = 1
                for attack in self.player.pokemon.attacks:
                    print(f"{count}: {attack.name} - {attack.damage} dmg - {attack.accuracy}% accuracy")
                    count += 1
                print("--------------------")

                try:
                    attack = self.player.pokemon.attacks[int(getch()) - 1]

                    print(attack)
                except (ValueError, IndexError):
                    print("Invalid attack")

        return 0