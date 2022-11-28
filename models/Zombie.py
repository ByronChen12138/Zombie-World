import random

from models.Barrier import Barrier
from models.Character import Character
from database import *
from utils.utils import isCirclePositionLegal


class Zombie(Character):
    def __init__(self, x, y, direction, z_type):
        size, HP, speed, color, damage, heat_rate, self.appear_rate, self.score = Z_TYPE[z_type]
        super().__init__(x, y, size, direction, color, HP, speed, damage, heat_rate)
        self.z_type = z_type
        self.move_type = "Direct"
        self.type = "Zombie"

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

    def moveRandom(self, app):
        """
        Upd the direction for the next move randomly
        :param app: current app
        :return: None
        """
        index = random.randint(0, 7)
        self.direction = DIRECTIONS[DIRECTIONS_LIST[index]]

    def moveDirect(self, app):
        """
        Upd the direction for the next move directly to the player
        :param app: current app
        :return: None
        """
        if app.player.x < self.x:
            if app.player.y < self.y:
                self.direction = DIRECTIONS["Up-Left"]
            elif app.player.y == self.y:
                self.direction = DIRECTIONS["Left"]
            else:
                self.direction = DIRECTIONS["Down-Left"]

        elif app.player.x == self.x:
            if app.player.y < self.y:
                self.direction = DIRECTIONS["Up"]
            elif app.player.y == self.y:
                self.direction = (0, 0)
            else:
                self.direction = DIRECTIONS["Down"]

        else:
            if app.player.y <= self.y:
                self.direction = DIRECTIONS["Up-Right"]
            elif app.player.y == self.y:
                self.direction = DIRECTIONS["Right"]
            else:
                self.direction = DIRECTIONS["Down-Right"]

    def moveDFS(self, app):
        """
        Upd the direction for the next move using DFS
        :param app: current app
        :return: None
        """
        # TODO: do the dfs direction finding

    def move(self, app):
        if self.move_type == "Random":
            self.moveDirect(app)

        elif self.move_type == "Direct":
            self.moveDirect(app)

        else:
            self.moveDFS(app)

        ans = super().move(app)

        if not ans:
            # If not moving on the map, attack possible barrier
            dx, dy = self.direction
            new_x = self.x - dx
            new_y = self.y - dy

            is_movable, barrier = isCirclePositionLegal(app, new_x, new_y, self.size)

            if barrier and isinstance(barrier, Barrier):
                self.attack(barrier)
                if barrier.isBroken(app):
                    app.map.removeAnObj(barrier)

        return ans
