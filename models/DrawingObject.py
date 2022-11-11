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

    def drawObject(self, app, canvas, start_canvas_x, start_canvas_y, cell_size):
        size = self.size * cell_size
        # TODO: Something is going wrong with this calculation
        if self.shape == "Circle":
            left_x = start_canvas_x + cell_size * (self.x - self.size + 1)
            up_y = start_canvas_y + cell_size * (99 - self.y + self.size - 1)
            canvas.create_oval(left_x, up_y, left_x + self.size * cell_size, up_y + self.size * cell_size, fill=self.color, outline='black')
