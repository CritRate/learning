from typing import Iterable

from .singly_linked_list import SinglyLinkedList


class Stack:

    def __init__(self):
        """
        Create Stack
        """
        self.list = SinglyLinkedList()

    @classmethod
    def with_starting_values(cls, data: Iterable):
        """
        Create Stack with starting values from Iterable source

        :param Iterable data: Iterable to populate the stack with.
        :return: Stack
        :rtype: Stack
        """
        stack = cls()
        for value in data:
            stack.push(value)
        return stack

    def push(self, data: object):
        """
        Push data to the top of the stack.

        :param object data: Data to push on top
        :return:
        """
        self.list.add_first(data=data)

    def pop(self) -> object:
        """
        Returns and removes the top data from stack.

        :return:
        :rtype: object
        """
        if self.is_empty:
            raise RuntimeError('Stack is empty')
        return self.list.remove_first()

    def peek(self) -> object:
        """
        Returns and does not remove the top data from stack

        :return:
        :rtype: object
        """
        if self.is_empty:
            raise RuntimeError('Stack is empty')
        return self.list.peek_first()

    @property
    def is_empty(self):
        """
        Checks whether the stack is empty or not.

        :return:
        """
        return self.list.is_empty

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)

    def __iter__(self):
        return iter(self.list)
