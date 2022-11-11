from utils.utils import *
from models.Character import Character


class Player(Character):
    def __init__(self):
        size, ammo, heat_rate, color, damage, appear_rate = G_TYPE["Pistol"]
        super().__init__(50, 50, 3, (0, 1), "black", 100, 1, damage, appear_rate)
        self.guns = {"Pistol"}
        self.barriers = {"Box": 100, "Oil Drum": 10}
