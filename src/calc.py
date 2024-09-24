"""
Task 3: Calculator using design patterns
"""


class Operation:
    def execute(self, a, b):
        raise NotImplementedError


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Substract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Devide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot devide by zero!")

        return a / b


class Calculator:
    def __init__(self):
        self.operations = {
            "+": Add(),
            "-": Substract(),
            "*": Multiply(),
            "/": Devide(),
        }

    def calculate(self, operator, a, b):
        if operator not in self.operations:
            raise ValueError(f"Unknown operator: {operator}")

        return self.operations[operator].execute(a, b)
