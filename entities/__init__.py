from enum import Enum

class Attack:
    name: str
    damage: int
    accuracy: int
    
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy

class Entity:
    name: str
    hp: int
    max_hp: int
    x: int
    y: int

    def __init__(self) -> None:
        pass

    def get_name(self) -> str:
        return self.name.capitalize()
    
    def get_hp(self) -> int:
        return self.hp
    
    def get_max_hp(self) -> int:
        return self.max_hp
    
    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y

    def set_x(self, x: int) -> None:
        self.x = x
    
    def set_y(self, y: int) -> None:
        self.y = y

class Pokemon(Entity):
    attacks: list[Attack]
    level: int
    exp: int

    def __init__(self, name: str, max_hp: int, hp: int, level: int, exp: int, attacks: list[Attack]):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.attacks = attacks
        self.level = level
        self.exp = exp
    
    def get_name(self) -> str:
        if self.name == "":
            return self.pokemon_type.value.capitalize()
        return self.name.capitalize()

    def attack(attack: Attack, target) -> bool:
        pass

class Player(Entity):
    pokemon: Pokemon

    def __init__(self, name: str, pokemon: Pokemon):
        self.name = name
        self.pokemon = pokemon

class Pikachu(Pokemon):
    def __init__(self, level: int, exp: int):
        super().__init__("Pikachu", 250, 250, level, exp, [
            Attack("Thunder Shock", 40, 100),
            Attack("Quick Attack", 40, 100),
            Attack("Thunderbolt", 90, 100),
            Attack("Thunder", 110, 70)
        ])

pokemon: dict[Pokemon] = {
    "Pikachu": Pikachu,
}