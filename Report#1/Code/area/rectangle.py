class Rectangle:
    def __init__(self, height, width):
        self.check_edge_value_validity(height)
        self.check_edge_value_validity(width)
        self.height = height
        self.width = width

    def compute_area(self):
        return self.height * self.width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.check_edge_value_validity(height)
        self.height = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.check_edge_value_validity(width)
        self.width = width

    def check_edge_value_validity(self, edge):
        if not self.is_integer_or_float(edge):
            raise InvalidEdgeType
        if edge <= 0:
            raise ZeroEdgeError

    def is_integer_or_float(self, number):
        return type(number) == int or type(number) == float


class InvalidEdgeType(Exception):
    pass


class ZeroEdgeError(Exception):
    pass
