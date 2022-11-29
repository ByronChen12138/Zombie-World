from models.Barrier import Barrier
from models.DrawingObject import DrawingObject
from utils.utils import *


class Map(DrawingObject):
    def __init__(self, x, y, size, player):
        super().__init__(x, y, size, "Circle", (1, 0), "black")
        self.player = player
        self.map = [[None for _ in range(MAP_BLOCKS)] for _ in range(MAP_BLOCKS)]
        self.createNewMap()
        self.type = "Map"

    def __str__(self):
        """
        Good for debugging
        :return: str of all the map
        """
        # Citation: https://stackoverflow.com/questions/13214809/pretty-print-2d-list
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.map])

    def getMap(self):
        return self.map

    def createAnObj(self, obj):
        """
        Create an object on the map
        :param obj: object to be created
        :return: None
        """
        for i in range(obj.x - obj.size // 2, obj.x + obj.size // 2 + 1):
            for j in range(obj.y - obj.size // 2, obj.y + obj.size // 2 + 1):
                if 0 <= i <= MAP_BLOCKS - 1 and 0 <= j <= MAP_BLOCKS - 1:
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
                if 0 <= i <= MAP_BLOCKS - 1 and 0 <= j <= MAP_BLOCKS - 1:
                    if self.map[j][i] is not None:
                        return False

        barrier = Barrier(x, y, (1, 0), b_type)
        self.createAnObj(barrier)

        return True

    def createNewMap(self):
        """
        Create a new map with None and number of walls
        :return: None
        """
        self.createAnObj(self.player)

        for i in range(NUM_OF_WALL):
            x = random.randint(0, MAP_BLOCKS - 1)
            y = random.randint(0, MAP_BLOCKS - 1)
            while not self.createABarrier(x, y, "Wall"):
                x = random.randint(0, MAP_BLOCKS - 1)
                y = random.randint(0, MAP_BLOCKS - 1)

    def removeAnObj(self, obj):
        """
        Remove obj from the map
        :param obj: Obj to be deleted
        :return:
        """

        for i in range(obj.x - obj.size // 2, obj.x + obj.size // 2 + 1):
            for j in range(obj.y - obj.size // 2, obj.y + obj.size // 2 + 1):
                if 0 <= i <= MAP_BLOCKS - 1 and 0 <= j <= MAP_BLOCKS - 1:
                    self.map[j][i] = None

    def anyBarrier(self, x, y, size):
        for i in range(x - size // 2, x + size // 2 + 1):
            for j in range(y - size // 2, y + size // 2 + 1):
                if 0 <= i <= MAP_BLOCKS - 1 and 0 <= j <= MAP_BLOCKS - 1:
                    if isinstance(self.map[j][i], Barrier):
                        return self.map[j][i]
        return None

    def getSurroundings(self, obj, r):
        ans = set()
        for i in range(obj.x - 1 - r, obj.x + 2 + r):
            for j in range(obj.y - 1 - r, obj.y + 2 + r):
                if 0 <= i <= MAP_BLOCKS - 1 and 0 <= j <= MAP_BLOCKS - 1:
                    if self.map[j][i] is not None:
                        ans.add(self.map[j][i])
        return ans
