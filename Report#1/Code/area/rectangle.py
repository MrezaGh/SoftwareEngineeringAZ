class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def compute_area(self):
        return -1


class InvalidEdgeType(Exception):
    pass


class ZeroEdgeError(Exception):
    pass
