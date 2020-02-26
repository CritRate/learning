from typing import Any, Optional


class Node:
    """
    Class representing internal structure for Singly linked list
    """

    def __init__(self, data: object, next: 'Node' = None):
        """

        :param object data: Data saved in the node
        :param Node next: Reference to the next node
        """
        self.data: Any = data
        self.next: 'Node' = next


class SinglyLinkedList:
    """
    Implementation of Singly linked list data structure
    """

    def __init__(self):
        self.size: int = 0
        # Start of the list
        self.head: Optional['Node'] = None
        # End of the list
        self.tail: Optional['Node'] = None

    def add_last(self, data: object):
        """
        Add data to the end of the list

        :param object data:  Data to be inserted
        :return:
        """
        if self.is_empty:
            self.head = self.tail = Node(data=data)
        else:
            self.tail.next = Node(data=data)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, data: object):
        """
        Add data to the start of the list

        :param object data: Data to be inserted
        :return:
        """
        if self.is_empty:
            self.head = self.tail = Node(data=data)
        else:
            self.head = Node(data=data, next=self.head)
        self.size += 1

    def add(self, data: object, index: int):
        """
        Add data at the specified index

        :param data: Data to add
        :param index: Specifies at what index to add the value
        :return:
        """
        if index > self.size or index < 0:
            raise IndexError()
        if index == 0:
            self.add_first(data)
        elif index == self.size:
            self.add_last(data)
            # adding in-between
        else:
            position = 1
            trav = self.head
            while trav:
                if position == index:
                    next_trav = Node(data=data, next=trav.next)
                    trav.next = next_trav
                    break
                trav = trav.next
                position += 1
        self.size += 1

    def remove_last(self) -> object:
        """
        Remove the last element of the list

        :return: Returns the data of the last element
        """
        if self.is_empty:
            raise RuntimeError('Empty list')
        trav = self.head
        while trav:
            if trav.next == self.tail:
                data = self.tail.data
                trav.next = None
                self.tail = trav
                self.size -= 1
                return data
            trav = trav.next

    def remove_first(self):
        """
        Remove the first element of the list

        :return: Returns the first element of the list
        """
        if self.is_empty:
            raise RuntimeError('Empty list')
        #  get the next node
        node = self.head.next
        data = self.head.data
        #  remove the first node references
        self.head.next = None
        #  set new head
        self.head = node
        self.size -= 1
        return data

    def remove(self, index: int) -> object:
        """
        Remove data at specified index

        :param index: Data to be removed at index
        :return: Removed value at the specified index
        """
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            return self.remove_first()
        elif index == self.size - 1:
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
                    self.size -= 1
                    return removed
                trav = trav.next
                position += 1

    def peek_first(self):
        """
        Returns the first element of the list without removing it

        :return: Returns the first element of the list
        """
        if self.is_empty:
            return None
        return self.head.data

    def peek_last(self):
        """
        Returns the last element of the list without removing it

        :return: Returns the last element of the list
        """
        if self.is_empty:
            return None
        return self.tail.data

    def peek(self, index) -> object:
        """
        Returns value at specified index but does not remove or modify it

        :param index:
        :return: Value at the specified index
        """
        if index < 0 or index > self.size:
            raise IndexError()
        if index == 0:
            return self.peek_first()
        elif index == self.size - 1:
            return self.peek_last()
        else:
            position = 0
            trav = self.head
            while trav:
                if position == index:
                    return trav.data
                trav = trav.next
                position += 1

    def indexof(self, data: object) -> int:
        """
        Find the position of the data in the list. If there are multiple, it return the first one.
        If data is not found in the list, returns -1.

        :param data: Specified data to be found in list
        :return: Return the position of the data in the list
        :rtype: int
        """
        if self.is_empty:
            return -1
        elif self.head.data == data:
            return 0
        trav = self.head.next
        position = 1
        while trav:
            if trav.data == data:
                return position
            trav = trav.next
            position += 1
        return -1

    def clear(self):
        """
        Remove all the elements of the list

        :return:
        """
        trav = self.head
        while trav:
            node = trav.next
            # Remove all the references to Nodes
            trav.next = None
            trav = node
        self.head = None
        self.tail = None

    @property
    def is_empty(self) -> bool:
        """
        Returns if the list is empty

        :return:
        """
        return not bool(self.size)

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
