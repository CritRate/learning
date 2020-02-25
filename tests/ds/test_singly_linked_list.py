import unittest

from ds.singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.list = SinglyLinkedList()
        self.list.add_last(5)
        self.list.add_last(10)
        self.list.add_last(7)
        self.list.add_last(8)
        self.list.add_last(1)

    def test_length_of_list(self):
        self.assertEqual(len(self.list), 5)

    def test_str_of_list(self):
        self.assertEqual(str(self.list), '[5, 10, 7, 8, 1]')

    def test_iterator_list(self):
        self.assertEqual([x for x in self.list], [5, 10, 7, 8, 1])

    def test_add_first_empty(self):
        _list = SinglyLinkedList()
        _list.add_first(10)
        self.assertEqual([x for x in _list], [10])

    def test_add_last_empty(self):
        _list = SinglyLinkedList()
        _list.add_last(10)
        self.assertEqual([x for x in _list], [10])

    def test_add_last_values(self):
        self.list.add_last(15)
        self.assertEqual([x for x in self.list], [5, 10, 7, 8, 1, 15])

    def test_add_first_values(self):
        self.list.add_first(15)
        self.assertEqual([x for x in self.list], [15, 5, 10, 7, 8, 1])

    def test_remove_last(self):
        self.list.remove_last()
        self.assertEqual([x for x in self.list], [5, 10, 7, 8])

    def test_remove_last_from_empty(self):
        empty_list = SinglyLinkedList()
        with self.assertRaises(RuntimeError):
            empty_list.remove_last()

    def test_remove_first(self):
        self.list.remove_first()
        self.assertEqual([x for x in self.list], [10, 7, 8, 1])

    def test_remove_first_from_empty(self):
        empty_list = SinglyLinkedList()
        with self.assertRaises(RuntimeError):
            empty_list.remove_first()

    def test_is_not_empty(self):
        self.assertFalse(self.list.is_empty)

    def test_is_empty(self):
        _list = SinglyLinkedList()
        self.assertTrue(_list.is_empty)

    def test_peek_first(self):
        self.assertEqual(self.list.peek_first(), 5)

    def test_peek_first_empty(self):
        _list = SinglyLinkedList()
        self.assertIsNone(_list.peek_first())

    def test_peek_last(self):
        self.assertEqual(self.list.peek_last(), 1)

    def test_peek_last_empty(self):
        _list = SinglyLinkedList()
        self.assertIsNone(_list.peek_last())

    def test_add_at_index(self):
        self.list.add(20, 2)
        self.assertEqual([x for x in self.list], [5, 10, 20, 7, 8, 1])

    def test_add_at_index_too_low(self):
        with self.assertRaises(IndexError):
            self.list.add(10, -1)

    def test_add_at_index_too_high(self):
        with self.assertRaises(IndexError):
            self.list.add(10, 10)

    def test_add_at_index_first(self):
        _list = SinglyLinkedList()
        _list.add(1, 0)
        self.assertEqual([x for x in _list], [1])

    def test_add_at_index_last(self):
        _list = SinglyLinkedList()
        _list.add_last(1)
        _list.add_last(10)
        _list.add(5, 2)
        self.assertEqual([x for x in _list], [1, 10, 5])

    def test_remove_at_index(self):
        data = self.list.remove(2)
        self.assertEqual(data, 7)
        self.assertEqual([x for x in self.list], [5, 10, 8, 1])

    def test_remove_at_index_low(self):
        _list = SinglyLinkedList()
        with self.assertRaises(IndexError):
            _list.remove(-1)

    def test_remove_at_index_high(self):
        _list = SinglyLinkedList()
        with self.assertRaises(IndexError):
            _list.remove(10)

    def test_remove_at_index_last(self):
        data = self.list.remove(4)
        self.assertEqual(data, 1)
        self.assertEqual([x for x in self.list], [5, 10, 7, 8])

    def test_remove_at_index_first(self):
        data = self.list.remove(0)
        self.assertEqual(data, 5)
        self.assertEqual([x for x in self.list], [10, 7, 8, 1])

    def test_clear(self):
        self.list.clear()
        self.assertEqual([x for x in self.list], [])

    def test_peek_at_index(self):
        data = self.list.peek(2)
        self.assertEqual(data, 7)

    def test_peek_at_index_first(self):
        data = self.list.peek(0)
        self.assertEqual(data, 5)

    def test_peek_at_index_last(self):
        data = self.list.peek(4)
        self.assertEqual(data, 1)

    def test_peek_at_index_low(self):
        with self.assertRaises(IndexError):
            self.list.peek(-1)

    def test_peek_at_index_high(self):
        with self.assertRaises(IndexError):
            self.list.peek(10)
