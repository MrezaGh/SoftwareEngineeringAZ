from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def compute_area(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def set_width(self, width):
        pass