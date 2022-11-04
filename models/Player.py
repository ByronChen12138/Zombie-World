from models.Character import Character


class Player(Character):
    def __init__(self):
        super().__init__(50, 50, 4, (0, 1), "black", 100, 1)
        self.guns = set()
        self.barriers = {"Box": 100, "Oil Drum": 10}
