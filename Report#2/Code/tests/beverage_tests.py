import pytest
from decorator.coffee_shop import *


class TestBeverage:

    def test_house_blend(self):
        # Pure HouseBlend
        beverage = HouseBlend()
        assert beverage.get_description() == "Delicious HouseBlend"
        assert beverage.cost() == 0.89

    def test_espresso(self):
        # Pure Espresso
        beverage = Espresso()
        assert beverage.get_description() == "Delicious Espresso"
        assert beverage.cost() == 1.99

    def test_house_blend_with_steamed_milk(self):
        # HouseBlend + SteamedMilk
        beverage = SteamedMilk(HouseBlend())
        assert beverage.get_description() == "Delicious HouseBlend with milk"
        assert beverage.cost() == 0.89 + 0.1

    def test_espresso_with_mocha_and_whip(self):
        # Espresso + Mocha + Whip
        beverage = Whip(Mocha(Espresso()))
        assert beverage.get_description() == "Delicious Espresso with mocha with whip"
        assert beverage.cost() == 1.99 + 0.2 + 0.1

    def test_espresso_with_double_mocha_and_whip_and_steamed_milk(self):
        # Espresso + Mocha + Mocha + Whip + SteamedMilk
        beverage = SteamedMilk(Whip(Mocha(Mocha(Espresso()))))
        assert beverage.get_description() == "Delicious Espresso with mocha with mocha with whip with milk"
        assert beverage.cost() == 1.99 + 0.2 + 0.2 + 0.1 + 0.1
