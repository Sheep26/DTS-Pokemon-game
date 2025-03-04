from attack import *
from enum import Enum

class Entity:
    name: str
    hp: int
    max_hp: int

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
    

class PokemonType(Enum):
    PIKACHU = 0
    CHARMANDER = 1
    SQUIRTLE = 2
    BULBASAUR = 3

class Pokemon(Entity):
    pokemon_type: PokemonType
    attacks: list[Attack]

    def __init__(self, name: str, max_hp: int, hp: int, attacks: list[Attack], pokemon_type: PokemonType):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.attacks = attacks
        self.pokemon_type = pokemon_type
    
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