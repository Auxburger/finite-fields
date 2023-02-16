import math
from typing import List

from fields.extension_field_element import ExtensionFieldElement
from fields.finite_field import FiniteField


class ExtensionField:
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.q = math.ceil(math.pow(p, n))
        self.finite_field = FiniteField(self.p)
        elements = []
        for i in range(self.q):
            elements.append(ExtensionFieldElement(i, self))
        print("Elements of F", self.q, elements)
        self.elements = elements
        print(self.get_additive_table())

    def get_extension_table(self, label: str, values: List[any]):
        table = label
        table += "".join(" " for i in range(self.n - 1))
        table += " | "
        for i in range(self.q):
            table += str(self.elements[i])
            table += " "
        table += "\n"
        for i in range(len(table) - 2):
            table += "-"
        for i in range(self.q):
            table += "\n"
            table += str(self.elements[i])
            table += " | "
            for j in range(self.q):
                table += str(values[i * self.q + j])
                table += " "
        return table

    def get_additive_table(self):
        additive_values = []
        for i in range(self.q):
            for j in range(self.q):
                additive_values.append(self.elements[i] + self.elements[j])
        return self.get_extension_table("+", additive_values)

    def get_multiplicative_table(self):
        additive_values = []
        for i in range(self.q):
            for j in range(self.q):
                additive_values.append(self.elements[i] * self.elements[j])
        return self.get_extension_table("*", additive_values)
