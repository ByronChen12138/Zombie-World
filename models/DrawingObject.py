from utils.utils import *


class DrawingObject:
    def __init__(self, x, y, size, shape, direction, color):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.direction = direction
        self.color = color

    def getPosition(self):
        return self.x, self.y

    def getSize(self):
        return self.size

    def getDirection(self):
        return self.direction

    def drawObject(self, app, canvas, cell_size):
        drawing_size = self.size * cell_size
        cx, cy = getMapCXY(app, self.x, self.y)

        if self.shape == "Circle":
            drawing_size /= 2
            canvas.create_oval(cx - drawing_size, cy - drawing_size, cx + drawing_size,
                               cy + drawing_size, fill=self.color, outline='black')

            if self.color == "black" or self.color == "#DB1EF1":
                dx, dy = self.getDirection()
                dx *= 2
                dy *= 2
                canvas.create_line(cx - dx * drawing_size, cy - dy * drawing_size,
                                   cx, cy, fill=self.color, width=3)

        elif self.shape == "Gun":
            canvas.create_polygon(cx, cy,
                                  cx, cy + cell_size * 1.5,
                                  cx + cell_size * 1.5, cy + cell_size * 1.5,
                                  cx + cell_size * 1.5, cy - cell_size * 1.5,
                                  cx - cell_size * 1.5, cy - cell_size * 1.5,
                                  cx - cell_size * 1.5, cy, fill=self.color, outline="black")
