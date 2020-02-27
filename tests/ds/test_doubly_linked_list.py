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

    def test_add_first_empty(self):
        _list = DoublyLinkedList()
        _list.add_first(1)
        self.assertEqual([x for x in _list], [1])

    def test_add_at_index_lower_half(self):
        self.list.add(6, 2)
        self.assertEqual([x for x in self.list], [1, 2, 6, 3, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 6, 2, 1])

    def test_add_at_index_upper_half(self):
        self.list.add(6, 4)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 6, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 6, 4, 3, 2, 1])

    def test_add_at_index_too_low(self):
        with self.assertRaises(IndexError):
            self.list.add(6, -1)

    def test_add_at_index_too_high(self):
        with self.assertRaises(IndexError):
            self.list.add(6, len(self.list) + 1)

    def test_add_at_index_zero(self):
        self.list.add(0, 0)
        self.assertEqual([x for x in self.list], [0, 1, 2, 3, 4, 5])

    def test_add_at_index_max(self):
        self.list.add(6, len(self.list))
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5, 6])

    def test_clear(self):
        self.list.clear()
        self.assertEqual([x for x in self.list], [])
        self.assertEqual(len(self.list), 0)

    def test_peek_last(self):
        self.assertEqual(self.list.peek_last(), 5)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_first(self):
        self.assertEqual(self.list.peek_first(), 1)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_last_empty(self):
        _list = DoublyLinkedList()
        self.assertIsNone(_list.peek_last())

    def test_peek_first_empty(self):
        _list = DoublyLinkedList()
        self.assertIsNone(_list.peek_first())

    def test_peek_lower(self):
        self.assertEqual(self.list.peek(1), 2)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_upper(self):
        self.assertEqual(self.list.peek(3), 4)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_zero(self):
        self.assertEqual(self.list.peek(0), 1)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_max(self):
        self.assertEqual(self.list.peek(len(self.list) - 1), 5)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4, 5])

    def test_peek_empty_list(self):
        with self.assertRaises(IndexError):
            _list = DoublyLinkedList()
            _list.peek(0)

    def test_peek_too_low(self):
        with self.assertRaises(IndexError):
            self.list.peek(-1)

    def test_peek_too_high(self):
        with self.assertRaises(IndexError):
            self.list.peek(len(self.list))

    def test_remove_last_one_item(self):
        _list = DoublyLinkedList()
        _list.add_first(1)
        self.assertEqual([x for x in _list], [1])
        data = _list.remove_last()
        self.assertEqual(data, 1)
        self.assertEqual([x for x in _list], [])
        self.assertEqual([x for x in reversed(_list)], [])

    def test_remove_last_empty(self):
        with self.assertRaises(RuntimeError):
            _list = DoublyLinkedList()
            _list.remove_last()

    def test_remove_last(self):
        data = self.list.remove_last()
        self.assertEqual(data, 5)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4])
        self.assertEqual([x for x in reversed(self.list)], [4, 3, 2, 1])

    def test_remove_first_one_item(self):
        _list = DoublyLinkedList()
        _list.add_first(1)
        self.assertEqual([x for x in _list], [1])
        data = _list.remove_first()
        self.assertEqual(data, 1)
        self.assertEqual([x for x in _list], [])
        self.assertEqual([x for x in reversed(_list)], [])

    def test_remove_first_empty(self):
        with self.assertRaises(RuntimeError):
            _list = DoublyLinkedList()
            _list.remove_first()

    def test_remove_first(self):
        data = self.list.remove_first()
        self.assertEqual(data, 1)
        self.assertEqual([x for x in self.list], [2, 3, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 2])

    def test_remove_lower(self):
        data = self.list.remove(2)
        self.assertEqual(data, 3)
        self.assertEqual([x for x in self.list], [1, 2, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 2, 1])

    def test_remove_upper(self):
        data = self.list.remove(3)
        self.assertEqual(data, 4)
        self.assertEqual([x for x in self.list], [1, 2, 3, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 3, 2, 1])

    def test_remove_index_too_low(self):
        with self.assertRaises(IndexError):
            self.list.remove(-1)

    def test_remove_index_too_high(self):
        with self.assertRaises(IndexError):
            self.list.remove(len(self.list))

    def test_remove_at_index_first(self):
        data = self.list.remove(0)
        self.assertEqual(data, 1)
        self.assertEqual([x for x in self.list], [2, 3, 4, 5])
        self.assertEqual([x for x in reversed(self.list)], [5, 4, 3, 2])

    def test_remove_at_index_end(self):
        data = self.list.remove(len(self.list) - 1)
        self.assertEqual(data, 5)
        self.assertEqual([x for x in self.list], [1, 2, 3, 4])
        self.assertEqual([x for x in reversed(self.list)], [4, 3, 2, 1])
