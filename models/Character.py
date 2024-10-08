from models.DrawingObject import DrawingObject
from utils.utils import *


class Character(DrawingObject):
    def __init__(self, x, y, size, direction, color, HP, speed, damage, heat_rate):
        super().__init__(x, y, size, "Circle", direction, color)
        self.HP = HP
        self.speed = speed
        self.damage = damage
        self.heat_rate = heat_rate
        self.move_time = 0

    def getHP(self):
        return self.HP

    def getSpeed(self):
        return self.speed

    def getDamage(self):
        return self.damage

    def getHeatRate(self):
        return self.heat_rate

    def move(self, app):
        """
        Move the character to the direction heading to
        :return: True if succeed to move, False if not
        """
        dx, dy = self.direction
        new_x = self.x - dx
        new_y = self.y - dy

        is_movable, barrier = isCirclePositionLegal(app, new_x, new_y, self.size)
        if is_movable:
            # Upd on the map
            app.map.removeAnObj(self)

            self.x = new_x
            self.y = new_y
            self.move_time = self.speed
            app.map.createAnObj(self)
            return True

        return False

    def isDied(self):
        """
        If the HP goes to 0, die
        :return: True if died, False if not
        """
        return self.HP <= 0
