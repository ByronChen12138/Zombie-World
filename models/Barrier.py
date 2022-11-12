from utils.utils import *
from models.DrawingObject import DrawingObject


class Barrier(DrawingObject):
    def __init__(self, x, y, direction, b_type):
        size, HP, color = B_TYPE[b_type]
        super().__init__(x, y, size, "Square", direction, color)
        self.HP = HP

    def getHP(self):
        return self.HP
