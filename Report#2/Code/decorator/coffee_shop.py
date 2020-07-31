from abc import abstractmethod, ABC


class Beverage(ABC):
    description = "generic beverage"

    @classmethod
    def get_description(cls):
        return cls.description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):
    description = "Delicious HouseBlend"

    def cost(self):
        return 0.89


class Espresso(Beverage):
    description = "Delicious Espresso"

    def cost(self):
        return 1.99


class CondimentDecorator(Beverage, ABC):

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + " " + self.description


class SteamedMilk(CondimentDecorator):
    description = "with milk"

    def cost(self):
        return self._beverage.cost() + self.added_cost()

    @staticmethod
    def added_cost():
        return 0.1


class Whip(CondimentDecorator):
    description = "with whip"

    def cost(self):
        return self._beverage.cost() + self.added_cost()

    @staticmethod
    def added_cost():
        return 0.1


class Mocha(CondimentDecorator):
    description = "with mocha"

    def cost(self):
        return self._beverage.cost() + self.added_cost()

    @staticmethod
    def added_cost():
        return 0.2
