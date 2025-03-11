from enum import Enum
from random import choice, randint
from area import Area

class PokemonType:
    name: str
    weaknesses: list[str]
    strengths: list[str]

    def __init__(self, name: str, weaknesses: list[str], strengths: list[str]):
        self.name = name
        self.weaknesses = weaknesses
        self.strengths = strengths

class Normal(PokemonType):
    def __init__(self):
        super().__init__("Normal", ["Fighting"], [])

class Fighting(PokemonType):
    def __init__(self):
        super().__init__("Fighting", ["Flying", "Psychic", "Fairy"], ["Normal", "Rock", "Steel", "Ice", "Dark"])

class Flying(PokemonType):
    def __init__(self):
        super().__init__("Flying", ["Electric", "Ice", "Rock"], ["Fighting", "Bug", "Grass"])

class Water(PokemonType):
    def __init__(self):
        super().__init__("Water", ["Grass", "Electric"], ["Fire", "Ground", "Rock"])

class Grass(PokemonType):
    def __init__(self):
        super().__init__("Grass", ["Fire", "Ice", "Poison", "Flying", "Bug"], ["Water", "Ground", "Rock"])

class Poison(PokemonType):
    def __init__(self):
        super().__init__("Poison", ["Ground", "Psychic"], ["Grass", "Fairy"])

class Electric(PokemonType):
    def __init__(self):
        super().__init__("Electric", ["Ground"], ["Water", "Flying"])

class Fire(PokemonType):
    def __init__(self):
        super().__init__("Fire", ["Water", "Rock", "Ground"], ["Grass", "Bug", "Ice"])

class Ground(PokemonType):
    def __init__(self):
        super().__init__("Ground", ["Water", "Grass", "Ice"], ["Fire", "Electric", "Poison", "Rock", "Steel"])

class Psychic(PokemonType):
    def __init__(self):
        super().__init__("Psychic", ["Bug", "Ghost", "Dark"], ["Fighting", "Poison"])

class Rock(PokemonType):
    def __init__(self):
        super().__init__("Rock", ["Water", "Grass", "Fighting", "Ground", "Steel"], ["Fire", "Ice", "Flying", "Bug"])

class Ice(PokemonType):
    def __init__(self):
        super().__init__("Ice", ["Fire", "Fighting", "Rock", "Steel"], ["Grass", "Ground", "Flying", "Dragon"])

class Bug(PokemonType):
    def __init__(self):
        super().__init__("Bug", ["Fire", "Flying", "Rock"], ["Grass", "Psychic", "Dark"])

class Dragon(PokemonType):
    def __init__(self):
        super().__init__("Dragon", ["Ice", "Dragon", "Fairy"], ["Dragon"])

class Ghost(PokemonType):
    def __init__(self):
        super().__init__("Ghost", ["Ghost", "Dark"], ["Psychic", "Ghost"])

class Dark(PokemonType):
    def __init__(self):
        super().__init__("Dark", ["Fighting", "Bug", "Fairy"], ["Psychic", "Ghost"])

class Steel(PokemonType):
    def __init__(self):
        super().__init__("Steel", ["Fire", "Fighting", "Ground"], ["Ice", "Rock", "Fairy"])

class Fairy(PokemonType):
    def __init__(self):
        super().__init__("Fairy", ["Poison", "Steel"], ["Fighting", "Dragon", "Dark"])

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

    def __init__(self):
        pass

    def get_name(self) -> str:
        return self.name.capitalize()
    
    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self) -> bool:
        return self.hp > 0

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

    def attack(self, target: Entity, move: Attack) -> dict:
        # Calculate if the attack missed or not
        missed = randint(0, 100) > move.accuracy
        
        # The attack missed, return false to indicate that the attack was not successful
        if missed: return {"successful": False}

        multiplier = 1

        # Check if the enemy is weak to the players pokemon
        if target is Player:
            for weakness in target.pokemon.get_type().weaknesses:
                if weakness == self.pokemon_type.name:
                    # The enemy is weak to the players pokemon, make the attack stronger
                    multiplier = 2
                    break
        elif target is Pokemon:
            for weakness in target.get_type().weaknesses:
                if weakness == self.pokemon_type.name:
                    # The enemy is weak to the players pokemon, make the attack stronger
                    multiplier = 2
                    break
        
        # Make the enemy take damage
        target.take_damage(self.attack_dmg * (move.damage/100) * multiplier)

        # Return true to indicate that the attack was successful
        return {
            "successful": True,
            "multiplier": multiplier,
            "damage": self.attack_dmg * (move.damage/100) * multiplier
        }

    def pick_attack(self) -> Attack:
        # Return a random attack from the list of attacks
        return choice(self.attacks)
    
    def get_type_name(self) -> str:
        return self.pokemon_type.name.capitalize()

class Player(Entity):
    pokemon: Pokemon
    location: Area

    def __init__(self, name: str, pokemon: Pokemon):
        self.name = name
        self.pokemon = pokemon
        self.location = Area.Home

class Pikachu(Pokemon):
    def __init__(self, level: int, exp: int):
        # Call the super class constructor with the name, max_hp, level, exp, next_level_exp, pokemon_type, attack_dmg, and attacks
        super().__init__("Pikachu", int(35 * (level if level > 1 else 1) * (0.25 if level > 1 else 1)), level, exp, 0.25 * level * 100, Electric(), 55 * (level if level > 1 else 1) * (0.25 if level > 1 else 1), [
            Attack("Thunder Shock", 40, 100),
            Attack("Quick Attack", 40, 100),
            Attack("Thunderbolt", 90, 100),
            Attack("Thunder", 110, 70),
        ])

class Charmander(Pokemon):
    def __init__(self, level: int, exp: int):
        # Call the super class constructor with the name, max_hp, level, exp, next_level_exp, pokemon_type, attack_dmg, and attacks
        super().__init__("Charmander", int(39 * (level if level > 1 else 1) * (0.25 if level > 1 else 1)), level, exp, 0.25 * level * 100, Fire(), 52 * (level if level > 1 else 1) * (0.25 if level > 1 else 1), [
            Attack("Ember", 40, 100),
            Attack("Scratch", 40, 100),
            Attack("Flamethrower", 90, 100),
            Attack("Inferno", 100, 50),
        ])

pokemon: dict[Pokemon] = {
    "Pikachu": Pikachu,
    "Charmander": Charmander,
}