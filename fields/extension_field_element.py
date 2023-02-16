from typing import List


class ExtensionFieldElement:
    def __repr__(self):
        finite_string = ""
        for i in self.finite_element:
            finite_string += str(i)
        return finite_string

    def __init__(self, index, extension_field):
        self.index = index
        self.extension_field = extension_field
        self.p = extension_field.p
        self.n = extension_field.n
        self.q = extension_field.q
        self.finite_element = self.compute_field_coefficients()

    def compute_field_coefficients(self):
        p_number = ""
        index = self.index
        elements = []
        while index > 0:
            remainder = index % self.p
            elements.append(remainder)
            p_number = str(remainder) + p_number
            index //= self.p
        for i in range(self.n - len(elements)):
            elements.append(0)

        elements.reverse()
        return elements

    def __add__(self, other: "ExtensionFieldElement"):
        resulting = self.finite_element.copy()
        for i in range(self.n):
            resulting[i] = resulting[i] + other.finite_element[i]
            resulting[i] %= self.p
        return self.extension_field.elements[self.to_decimal(resulting)]

    def __mul__(self, other: "ExtensionFieldElement"):
        resulting = self.finite_element.copy()
        for i in range(self.n):
            resulting[i] = resulting[i] * other.finite_element[i]
            resulting[i] %= self.p
        return self.extension_field.elements[self.to_decimal(resulting)]

    def to_decimal(self, number: List[int]):
        return int("".join(str(i) for i in number), self.p)