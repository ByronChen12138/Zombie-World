import random

from models.Character import Character
from database import *
from utils.utils import isCirclePositionLegal


class Zombie(Character):
    def __init__(self, x, y, direction, z_type):
        size, HP, speed, color, damage, heat_rate, self.appear_rate, self.score = Z_TYPE[z_type]
        super().__init__(x, y, size, direction, color, HP, speed, damage, heat_rate)
        self.z_type = z_type

    def __str__(self):
        return self.z_type

    def getAppearRate(self):
        return self.appear_rate

    def getScore(self):
        return self.score

    def attack(self, character):
        """
        Attack the character with self damage
        :return: None
        """
        character.HP -= self.damage

    def move(self, app):
        if app.player.x <= self.x:
            if app.player.y <= self.y:
                self.direction = DIRECTIONS["Up-Left"]
            else:
                self.direction = DIRECTIONS["Down-Left"]
        else:
            if app.player.y <= self.y:
                self.direction = DIRECTIONS["Up-Right"]
            else:
                self.direction = DIRECTIONS["Down-Right"]

        ans = super().move(app)

        if not ans:
            # If not moving on the map, attack possible barrier
            dx, dy = self.direction
            new_x = self.x - dx
            new_y = self.y - dy

            is_movable, barrier = isCirclePositionLegal(app, new_x, new_y, self.size)

            if barrier:
                self.attack(barrier)

        return ans
