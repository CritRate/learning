from typing import Iterable, Optional

from .singly_linked_list import SinglyLinkedList


class Stack:

    def __init__(self, data: Optional[Iterable] = None):
        """
        Create Stack

        :param Iterable data: Data to add to the stack.
        """

        self.list = SinglyLinkedList()
        if data:
            for value in data:
                self.list.add_first(value)

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
