from database import *
from models.DrawingObject import DrawingObject


class Gun(DrawingObject):
    def __init__(self, x, y, g_type):
        size, ammo, heat_rate, color, damage, appear_rate = G_TYPE[g_type]
        super().__init__(x, y, size, "Gun", (0, 1), color)
        self.ammo = ammo
        self.g_type = g_type
        self.heat_rate = heat_rate
        self.damage = damage
        self.appear_rate = appear_rate

    def getAmmo(self):
        return self.ammo

    def getType(self):
        return self.g_type
