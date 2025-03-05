from entities import Entity

class World():
    map: dict[int, int, str]
    entities: list[Entity]


# Create world instance and store the map in a dictionary holding a touple and a string
world: World = World(
    {
        (0, 0), "grass",
    }
)