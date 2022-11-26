from models.DrawingObject import DrawingObject
from utils.utils import *


class Bullet(DrawingObject):
    def __init__(self, x, y, direction, color, damage, speed):
        super().__init__(x, y, 1, "Circle", direction, color)
        self.damage = damage
        self.speed = speed
        # self.acceleration = 4

    def __str__(self):
        return f"({self.x}, {self.y})"

    def getDamage(self):
        return self.damage

    def move(self, app):
        """
        Move the bullet to the direction heading to
        :return: True if succeed to move, False if not
        """
        dx, dy = self.direction
        new_x = self.x - dx * self.speed  # * self.acceleration
        new_y = self.y - dy * self.speed  # * self.acceleration

        if isCirclePositionLegal(app, new_x, new_y, self.size):
            self.x = new_x
            self.y = new_y
            if 0 <= self.y < MAP_BLOCKS and \
                    0 <= self.x < MAP_BLOCKS:
                self.attack(app.map.getMap()[self.y][self.x])
            return True

        return False

    def attack(self, character):
        """
        Attack the character with self damage
        :return: None
        """
        if character is None:
            return
        character.HP -= self.damage
