from abc import ABC, abstractmethod


class Multiplication(ABC):

    @abstractmethod
    def calculate(self, first_param, second_param):
        pass


class NormalMultiplication(Multiplication):

    def calculate(self, first_param, second_param):
        return first_param * second_param


class LoopBasedMultiplication(Multiplication):

    def calculate(self, first_param, second_param):
        result = 0
        for _ in range(second_param):
            result += first_param
        return result


class Power(ABC):
    def __init__(self, multiplication: Multiplication):
        self.multiplication = multiplication

    @abstractmethod
    def calculate(self, number, power):
        pass


class RecursivePower(Power):

    def calculate(self, number, power):
        if power == 0:
            return 1
        return self.multiplication.calculate(number, self.calculate(number, power-1))


class LoopBasedPower(Power):

    def calculate(self, number, power):
        result = 1
        for _ in range(power):
            result *= number
        return result
