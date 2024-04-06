import re
import string

from app.rpn.pile import Stack


def subtract(left_operand, right_operand):
    return left_operand - right_operand


def addition(left_operand, right_operand):
    return left_operand + right_operand


def multiply(left_operand, right_operand):
    return left_operand * right_operand


def modulo(left_operand, right_operand):
    return left_operand % right_operand


def floor_divide(left_operand, right_operand):
    return left_operand // right_operand


def divide(left_operand, right_operand):
    return left_operand / right_operand


class Calculator:
    __operators = {
        '+': addition,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '//': floor_divide,
        '%': modulo,
    }

    def __init__(self):
        self.__stack = Stack()

    def evaluate_operator(self, element: string) -> bool:
        if element in self.__operators:
            right_operand = float(self.__stack.pop())
            left_operand = float(self.__stack.pop())
            result = self.__operators[element](left_operand, right_operand)
            self.__stack.push(str(result))
            return True
        else:
            return False

    def resolve(self, expression: string) -> string:
        # sanitize the string
        expression = expression.strip()

        # split to elements
        elements = re.split(' ', expression)
        for element in elements:
            if not self.evaluate_operator(element):
                self.__stack.push(element)

        # return result
        return self.__stack.pop()
