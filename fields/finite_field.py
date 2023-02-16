import numpy as np

from fields.math_helper import MathHelper


class FiniteElement:
    def __init__(self, number, finite_field):
        self.number = number
        self.finite_field = finite_field

    def __add__(self, other: "FiniteElement"):
        number = self.number + other.number
        number %= self.finite_field.p
        return self.finite_field.get_element(number)

    def __mul__(self, other: "FiniteElement"):
        number = self.number * other.number
        number %= self.finite_field.p
        return self.finite_field.get_element(number)


class FiniteField:
    def __init__(self, p):
        assert (MathHelper.is_prime(p))
        self.p = p
        self.elements = []
        for i in range(self.p):
            self.elements.append(FiniteElement(i, self))

    def get_element(self, number):
        return self.elements[number % self.p]

    def get_all_elements(self):
        return self.elements

    def find_generator(self):
        generators = []
        for x in self.elements:
            for y in self.elements:
                x * y
        return

    # element with a * b = 1
    def find_mul_inverse(self):
        for x in self.elements:
            for y in self.elements:
                if x * y == 1:
                    print(x, y)
        return

    # element with a + b = 0
    def find_add_inverse(self):
        for x in self.elements:
            for y in self.elements:
                if x + y == 0:
                    print(x, y)
        return
