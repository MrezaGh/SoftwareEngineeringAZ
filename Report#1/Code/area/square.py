from .shape import Shape
from .rectangle import InvalidEdgeType, ZeroEdgeError


class Square(Shape):
    def __init__(self, height=None, width=None):
        height, width = self.fill_width_and_height_if_not_given(height, width)
        self.check_is_square(height, width)
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
        self.width = height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.check_edge_value_validity(width)
        self.width = width
        self.height = self.height

    def check_edge_value_validity(self, edge):
        if not self.is_integer_or_float(edge):
            raise InvalidEdgeType
        if edge <= 0:
            raise ZeroEdgeError

    def is_integer_or_float(self, number):
        return type(number) == int or type(number) == float

    def check_is_square(self, height, width):
        if (height is None and width is None) or height != width:
            raise UnequalEdgesError

    def fill_width_and_height_if_not_given(self, height, width):
        if height is None:
            height = width
        elif width is None:
            width = height
        return height, width


class UnequalEdgesError(Exception):
    pass
