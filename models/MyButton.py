from utils.utils import *


class MyButton:
    def __init__(self, app, x, y, size, color, text):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.text = text
        cx, cy = getCXY(app, self.x, self.y)
        self.cx = cx
        self.cy = cy
        self.boundaries = [getCXY(app, self.x - self.size, self.y + self.size),
                           getCXY(app, self.x + self.size, self.y - self.size)]

    def getPosition(self):
        return self.x, self.y

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color

    def getText(self):
        return self.text

    def getBoundaries(self):
        return self.boundaries

    def draw(self, app, canvas):
        cx, cy = getCXY(app, self.x, self.y)
        self.cx = cx
        self.cy = cy
        self.boundaries = [getCXY(app, self.x - self.size, self.y + self.size),
                           getCXY(app, self.x + self.size, self.y - self.size)]

        canvas.create_rectangle(self.boundaries[0][0], self.boundaries[0][1],
                                self.boundaries[1][0], self.boundaries[1][1],
                                fill=self.color, outline='black', width=3)

        canvas.create_text(self.cx, self.cy, text=self.text,
                           fill='black', font='Times 20 bold italic')

    def isClick(self, x, y):
        p1, p2 = self.boundaries
        x1, y1 = p1
        x2, y2 = p2

        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        return False
