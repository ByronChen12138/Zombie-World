import random

from models.Character import Character
from database import *


class Zombie(Character):
    def __init__(self, x, y, direction, z_type):
        size, HP, speed, color, damage, heat_rate, self.appear_rate, self.score = Z_TYPE[z_type]
        super().__init__(x, y, size, direction, color, HP, speed, damage, heat_rate)
        self.z_type = z_type

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

        super().move(app)
