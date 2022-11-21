from models.Barrier import Barrier
from models.DrawingObject import DrawingObject
from utils.utils import *


class Map(DrawingObject):
    def __init__(self, x, y, size, player):
        super().__init__(x, y, size, "Circle", (1, 0), "black")
        self.player = player
        self.map = [[None for _ in range(MAP_BLOCKS)] for _ in range(MAP_BLOCKS)]
        self.createNewMap()

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.map])

    def getMap(self):
        return self.map

    def createAnObj(self, x, y, obj):
        """
        Create an object on the map
        :param x: x
        :param y: y
        :param obj: object to be created
        :return: None
        """
        for i in range(x - obj.size // 2, x + obj.size // 2 + 1):
            for j in range(y - obj.size // 2, y + obj.size // 2 + 1):
                if 0 <= i <= 99 and 0 <= j <= 99:
                    self.map[j][i] = obj

    def createABarrier(self, x, y, b_type):
        """
        Create a barrier in the map with 3x3 blocks
        :param x: x of barrier
        :param y: y of barrier
        :param b_type: Type of the barrier
        :return: True if success; else False
        """
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i <= 99 and 0 <= j <= 99:
                    if self.map[j][i] is not None:
                        return False

        barrier = Barrier(x, y, (1, 0), b_type)
        self.createAnObj(x, y, barrier)

        return True

    def createNewMap(self):
        """
        Create a new map with None and number of walls
        :return: None
        """
        self.createAnObj(50, 50, self.player)

        for i in range(NUM_OF_WALL):
            x = random.randint(0, 99)
            y = random.randint(0, 99)
            while not self.createABarrier(x, y, "Wall"):
                x = random.randint(0, 99)
                y = random.randint(0, 99)
