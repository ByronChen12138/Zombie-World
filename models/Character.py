from models.DrawingObject import DrawingObject
from utils.utils import *


class Character(DrawingObject):
    def __init__(self, x, y, size, direction, color, HP, speed):
        super().__init__(x, y, size, "Circle", direction, color)
        self.HP = HP
        self.speed = speed

    def getHP(self):
        return self.HP

    def getSpeed(self):
        return self.speed

    def move(self):
        """
        Move the character to the direction heading to
        :return: True if succeed to move, False if not
        """
        dx, dy = self.direction
        new_x = self.x + dx
        new_y = self.y + dy

        if isPositionLegal(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True

        return False
