import re
import string
from typing import Self


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


class Element:
    def __init__(self, value):
        self.__next = None
        self.__data = value

    def set_next(self, element):
        self.__next = element

    def get_data(self):
        return self.__data

    def get_next(self) -> Self | None:
        return self.__next


class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, elem: string) -> None:
        new_node = Element(elem)
        new_node.set_next(self.__head)
        self.__head = new_node
        self.__size += 1

    def pop(self) -> string:
        to_pop = self.__head
        self.__head = to_pop.get_next()
        return_value = to_pop.get_data()
        del to_pop
        self.__size -= 1
        return return_value

    def top(self) -> Element:
        return self.__head

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size


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
