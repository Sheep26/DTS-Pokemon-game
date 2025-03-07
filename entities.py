from enum import Enum
import random

class PokemonType(Enum):
    NORMAL = 0
    FIRE = 1
    FIGHTING = 2
    WATER = 3
    FLYING = 4
    GRASS = 5
    POISON = 6
    ELECTRIC = 7
    GROUND = 8
    PSYCHIC = 9
    ROCK = 10
    ICE = 11
    BUG = 12
    DRAGON = 13
    GHOST = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

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
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
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
    pokemon_type: PokemonType
    attack_dmg: int
    next_level_exp: int

    def __init__(self, name: str, max_hp: int, level: int, exp: int, next_level_exp: int, pokemon_type: PokemonType, attack_dmg: int, attacks: list[Attack]):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attacks = attacks
        self.level = level
        self.exp = exp
        self.pokemon_type = pokemon_type
        self.attack_dmg = attack_dmg

    def attack(self, move: Attack, target: Entity) -> bool:
        missed = random.randint(0, 100) > move.accuracy
        if missed: return False
        target.take_damage(self.attack_dmg * (move.damage/100))
        return True
    
    def get_type(self) -> PokemonType:
        return self.pokemon_type
    
    def get_type_name(self) -> str:
        return self.pokemon_type.name.capitalize()

class Player(Entity):
    pokemon: Pokemon

    def __init__(self, name: str, pokemon: Pokemon):
        self.name = name
        self.pokemon = pokemon

class Pikachu(Pokemon):
    def __init__(self, level: int, exp: int):
        super().__init__("Pikachu", 35, level, exp, (1 * (0.25 * level)) * 100, PokemonType.ELECTRIC, 55, [
            Attack("Thunder Shock", 40, 100),
            Attack("Quick Attack", 40, 100),
            Attack("Thunderbolt", 90, 100),
            Attack("Thunder", 110, 70)
        ])

class Charmander(Pokemon):
    def __init__(self, level: int, exp: int):
        super().__init__("Charmander", 39, level, exp, (1 * (0.25 * level)) * 100, PokemonType.FIRE, 52, [
            Attack("Ember", 40, 100),
            Attack("Scratch", 40, 100),
            Attack("Flamethrower", 90, 100),
            Attack("Inferno", 100, 50)
        ])

pokemon: dict[Pokemon] = {
    "Pikachu": Pikachu,
    "Charmander": Charmander,
}