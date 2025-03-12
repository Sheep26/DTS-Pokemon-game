class Area():
    name: str
    dialog: list[str]

    def __init__(self, name: str, dialog: list[str]):
        self.name = name
        self.dialog = dialog

class Area01(Area):
    def __init__(self):
        super().__init__("Area 01", [""])