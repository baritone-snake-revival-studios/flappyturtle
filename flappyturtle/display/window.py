class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dimensions = (width, height)

    def center(self):
        return [self.width / 2, self.height / 2]
