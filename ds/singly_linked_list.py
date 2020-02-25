from typing import Any, Optional
import sys


class Node:

    def __init__(self, data: Any, next: 'Node' = None):
        self.data: Any = data
        self.next: 'Node' = next


class SinglyLinkedList:

    def __init__(self):
        self.size: int = 0
        self.head: Optional['Node'] = None
        self.tail: Optional['Node'] = None

    def add_last(self, value):
        if self.is_empty:
            self.head = self.tail = Node(data=value)
        else:
            self.tail.next = Node(data=value)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, value):
        if self.is_empty:
            self.head = self.tail = Node(data=value)
        else:
            self.head = Node(data=value, next=self.head)
        self.size += 1

    def add(self, value: Any, index: int):
        """
        Add value at the specified index
        :param value: value to add
        :param index: specifies at what index to add the value
        :return: None
        """
        if index > self.size or index < 0:
            raise IndexError()
        if index == 0:
            self.add_first(value)
        elif index == self.size:
            self.add_last(value)
            # adding in-between
        else:
            position = 1
            trav = self.head
            while trav:
                if position == index:
                    next_trav = Node(data=value, next=trav.next)
                    trav.next = next_trav
                    break
                trav = trav.next
                position += 1
        self.size += 1

    def remove(self, index: int) -> Any:
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            return self.remove_first()
        elif index == self.size:
            return self.remove_last()
        else:
            position: int = 1
            trav: 'Node' = self.head
            while trav:
                if position == index:
                    node = trav.next.next
                    removed = trav.next.data
                    trav.next.next = None
                    trav.next = node
                    return removed
                trav = trav.next
                position += 1
        self.size -= 1

    def peek(self, index):
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            return self.peek_first()
        elif index == self.size:
            return self.peek_last()
        else:
            position = 0
            trav = self.head
            while trav:
                if position == index:
                    return trav.data
                trav = trav.next
                position += 1

    def clear(self):
        trav = self.head
        while trav:
            node = trav.next
            trav.next = None
            trav = node
        self.head = None
        self.tail = None

    def remove_last(self):
        if self.is_empty:
            raise RuntimeError('Empty list')
        trav = self.head
        while trav:
            if trav.next == self.tail:
                data = self.tail.data
                trav.next = None
                self.tail = trav
                return data
            trav = trav.next
        self.size -= 1

    def remove_first(self):
        if self.is_empty:
            raise RuntimeError('Empty list')
        #  get the next node
        node = self.head.next
        data = self.head.data
        #  remove all the first node references
        self.head.next = None
        #  set new head
        self.head = node
        self.size -= 1
        return data

    @property
    def is_empty(self):
        return not bool(self.size)

    def peek_first(self):
        if self.is_empty:
            return None
        return self.head.data

    def peek_last(self):
        if self.is_empty:
            return None
        return self.tail.data

    def __str__(self):
        trav = self.head
        output = '['
        while trav:
            if trav.next:
                output += f'{str(trav.data)}, '
            else:
                output += f'{str(trav.data)}'
            trav = trav.next
        output += ']'
        return output

    def __len__(self):
        return self.size

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next
