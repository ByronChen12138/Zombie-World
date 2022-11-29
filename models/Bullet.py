from models.Barrier import Barrier
from models.DrawingObject import DrawingObject
from utils.utils import *


class Bullet(DrawingObject):
    def __init__(self, x, y, direction, color, damage, speed, acceleration):
        super().__init__(x, y, 1, "Circle", direction, color)
        self.damage = damage
        self.speed = speed
        self.acceleration = acceleration

    def __str__(self):
        return f"({self.x}, {self.y})"

    def getDamage(self):
        return self.damage

    def deceleration(self):
        self.speed = self.speed - self.acceleration

    def move(self, app):
        """
        Move the bullet to the direction heading to
        :return: True if succeed to move, False if not
        """
        dx, dy = self.direction
        new_x = self.x - dx * self.speed
        new_y = self.y - dy * self.speed

        if isCirclePositionLegal(app, new_x, new_y, self.size):
            self.x = new_x
            self.y = new_y
            if 0 <= self.y < MAP_BLOCKS and \
                    0 <= self.x < MAP_BLOCKS:
                curr_block = app.map.getMap()[self.y][self.x]
                if curr_block and isinstance(curr_block, Barrier):
                    if curr_block.b_type == "Wall":
                        return False
                    self.attack(curr_block)
                    if curr_block.isBroken(app):
                        app.map.removeAnObj(curr_block)
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
