import pytest
from bridge.calculator import *


class TestPowerCalculator:

    def test_normal_multiplication(self):
        multiplier = NormalMultiplication()
        assert multiplier.__class__.__name__ == "NormalMultiplication"
        assert multiplier.calculate(4, 5) == 20

    def test_loop_based_multiplication(self):
        multiplier = LoopBasedMultiplication()
        assert multiplier.__class__.__name__ == "LoopBasedMultiplication"
        assert multiplier.calculate(4, 5) == 20

    def test_recursive_power_with_normal_multiplication(self):
        multiplier = NormalMultiplication()
        power = RecursivePower(multiplier)
        assert power.multiplication.__class__.__name__ == "NormalMultiplication"
        assert power.__class__.__name__ == "RecursivePower"
        assert power.calculate(number=5, power=3) == 125

    def test_recursive_power_with_loop_based_multiplication(self):
        multiplier = LoopBasedMultiplication()
        power = RecursivePower(multiplier)
        assert power.multiplication.__class__.__name__ == "LoopBasedMultiplication"
        assert power.__class__.__name__ == "RecursivePower"
        assert power.calculate(number=5, power=3) == 125

    def test_loop_based_power_with_normal_multiplication(self):
        multiplier = NormalMultiplication()
        power = LoopBasedPower(multiplier)
        assert power.multiplication.__class__.__name__ == "NormalMultiplication"
        assert power.__class__.__name__ == "LoopBasedPower"
        assert power.calculate(number=5, power=3) == 125

    def test_loop_based_power_with_loop_based_multiplication(self):
        multiplier = LoopBasedMultiplication()
        power = LoopBasedPower(multiplier)
        assert power.multiplication.__class__.__name__ == "LoopBasedMultiplication"
        assert power.__class__.__name__ == "LoopBasedPower"
        assert power.calculate(number=5, power=3) == 125

    def test_multiplication_constructor(self):
        try:
            multiplier = Multiplication()
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Multiplication with abstract methods calculate"
        else:
            pytest.fail("you should not be able to instantiate abstract class")

    def test_power_constructor(self):
        try:
            power = Power(None)
        except TypeError as e:
            assert str(e) == "Can't instantiate abstract class Power with abstract methods calculate"
        else:
            pytest.fail("you should not be able to instantiate abstract class")
