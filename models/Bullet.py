from models.DrawingObject import DrawingObject
from utils.utils import *


class Bullet(DrawingObject):
    def __init__(self, x, y, direction, color, damage, speed):
        super().__init__(x, y, 1, "Circle", direction, color)
        self.damage = damage
        self.speed = speed

    def getDamage(self):
        return self.damage

    def move(self):
        """
        Move the bullet to the direction heading to
        :return: True if succeed to move, False if not
        """
        dx, dy = self.direction
        new_x = self.x - dx * self.speed
        new_y = self.y - dy * self.speed

        if isPositionLegal(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True

        return False

    def attack(self, character):
        """
        Attack the character with self damage
        :return: None
        """
        character.HP -= self.damage
