from models.DrawingObject import DrawingObject


class Barrier(DrawingObject):
    def __init__(self, x, y, breakable, shape, direction, color):
        super().__init__(x, y, 3, shape, direction, color)
        self.breakable = breakable
        self.shape = "Square"

    def isBreakable(self):
        return self.breakable
