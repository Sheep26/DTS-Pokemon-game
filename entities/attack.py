class Attack:
    name: str
    damage: int
    accuracy: int
    
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy