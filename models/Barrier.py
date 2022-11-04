from models.DrawingObject import DrawingObject


class Barrier(DrawingObject):
    def __init__(self, x, y, breakable):
        self.x = x
        self.y = y
        self.size = 3
        self.breakable = breakable
        self.shape = "Square"

    def isBreakable(self):
        return self.breakable
