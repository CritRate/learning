import unittest

from ds.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.list = Stack()

    def test_str_stack(self):
        self.list.push(1)
        self.list.push(2)
        self.assertEqual(str(self.list), '[2, 1]')

    def test_iter_stack(self):
        self.list.push(1)
        self.list.push(2)
        self.assertEqual([x for x in self.list], [2, 1])

    def test_len_stack(self):
        self.list.push(1)
        self.list.push(2)
        self.assertEqual(len(self.list), 2)

    def test_stack_with_starting_data(self):
        _list = Stack([5, 4, 3])
        self.assertEqual([x for x in _list], [3, 4, 5])
        _list.push(1)
        self.assertEqual([x for x in _list], [1, 3, 4, 5])

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty)
        self.list.push(1)
        self.assertFalse(self.list.is_empty)

    def test_push_stack(self):
        self.list.push(1)
        self.assertEqual([x for x in self.list], [1])
        self.list.push(2)
        self.assertEqual([x for x in self.list], [2, 1])

    def test_pop_stack(self):
        self.list.push(1)
        self.list.push(2)
        self.list.push(3)
        data = self.list.pop()
        self.assertEqual(data, 3)
        self.assertEqual([x for x in self.list], [2, 1])
        self.list.push(10)
        self.list.push(100)
        self.list.pop()
        data = self.list.pop()
        self.assertEqual(data, 10)
        self.assertEqual([x for x in self.list], [2, 1])

    def test_pop_empty(self):
        with self.assertRaises(RuntimeError):
            self.list.push(1)
            self.list.pop()
            self.list.pop()

    def test_peek(self):
        self.list.push(1)
        self.list.push(2)
        data = self.list.peek()
        self.assertEqual(data, 2)

    def test_peek_empty(self):
        with self.assertRaises(RuntimeError):
            self.list.peek()
