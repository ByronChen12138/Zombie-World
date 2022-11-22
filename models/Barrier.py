from utils.utils import *
from models.DrawingObject import DrawingObject


class Barrier(DrawingObject):
    def __init__(self, x, y, direction, b_type):
        size, HP, color = B_TYPE[b_type]
        super().__init__(x, y, size, "Square", direction, color)
        self.HP = HP
        self.b_type = b_type

    def __str__(self):
        return self.b_type

    def getHP(self):
        return self.HP

    def getBType(self):
        return self.b_type

    def isBroken(self):
        """
        If the HP goes to 0, die
        :return: True if died, False if not
        """
        return self.HP <= 0
