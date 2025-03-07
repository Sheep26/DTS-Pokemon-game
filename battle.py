from entities import Player, Pokemon
from battletimer import Timer

class Battle:
    player: Player
    enemy: Pokemon

    def __init__(self, player: Player, enemy: Pokemon):
        self.player = player
        self.enemy = enemy

    def start(self):
        print(f"A wild {self.enemy.get_name()} appeared!")
        print(f"It's a {self.enemy.get_type_name()} type!")
        print(f"Level: {self.enemy.level}")
        print(f"HP: {self.enemy.get_hp()}/{self.enemy.get_max_hp()}")
        Timer(3).countdown()
        print("Go!")