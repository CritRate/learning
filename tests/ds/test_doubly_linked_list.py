import unittest

from ds.doubly_linked_list import DoublyLinkedList


class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.list = DoublyLinkedList()
        self.list.add_last(1)
        self.list.add_last(2)
        self.list.add_last(3)
        self.list.add_last(4)
        self.list.add_last(5)

    def test_list_iterator(self):
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_list_reversed(self):
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 2, 1])

    def test_str_doubly_linked_list(self):
        self.assertEqual(str(self.list), '[1, 2, 3, 4, 5]')

    def test_len_of_list(self):
        _list = DoublyLinkedList()
        self.assertEqual(len(_list), 0)
        _list.add_last(1)
        self.assertEqual(len(_list), 1)
        self.assertEqual(len(self.list), 5)
        self.list.add_last(6)
        self.assertEqual(len(self.list), 6)
        self.list.add_first(0)
        self.assertEqual(len(self.list), 7)
        self.list.add(1, 2)
        self.assertEqual(len(self.list), 8)
        self.list.add(1, 6)
        self.assertEqual(len(self.list), 9)

    def test_add_last(self):
        self.list.add_last(6)
        # check both prev and next references in Doubly linked list
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5, 6])
        self.assertEqual([x for x in reversed(self.list)], [6, 5, 4, 3, 2, 1])

    def test_add_last_empty(self):
        _list = DoublyLinkedList()
        _list.add_last(6)
        self.assertEqual([x for x in _list], [6])

    def test_add_first(self):
        self.list.add_first(0)
        # check both prev and next references in Doubly linked list
        self.assertEqual([x for x in self.list], [0, 1, 2, 3, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 2, 1, 0])

    def test_add_at_index_lower_half(self):
        self.list.add(6, 2)
        self.assertEqual([x for x in self.list], [1, 2, 6, 3, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 6, 2, 1])

    def test_add_at_index_upper_half(self):
        self.list.add(6, 4)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 6, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 6, 4, 3, 2, 1])

    def test_clear(self):
        self.list.clear()
        self.assertEqual([x for x in self.list], [])
        self.assertEqual(len(self.list), 0)
