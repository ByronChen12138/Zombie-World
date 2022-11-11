from models.Character import Character
from database import *


class Zombie(Character):
    def __init__(self, x, y, direction, z_type):
        size, HP, speed, color, damage, heat_rate, self.appear_rate = Z_TYPE[z_type]
        super().__init__(x, y, size, direction, color, HP, speed, damage, heat_rate)
        self.z_type = z_type

    def getAppearRate(self):
        return self.appear_rate
