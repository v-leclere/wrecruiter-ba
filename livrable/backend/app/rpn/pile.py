import string
from typing import Self


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
