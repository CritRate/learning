from typing import List
import unittest


def two_sum(numbers: List[int], target: int):
    # already checked numbers, no need for duplicates
    checked_numbers = set()
    result = []

    for num in numbers:
        # check if the difference is in the checked_numbers list
        x = target - num
        if x in checked_numbers:
            result.append((num, x))
        else:
            # if not add them
            checked_numbers.add(num)

    return result


class Test(unittest.TestCase):

    def test_two_sum(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(two_sum(numbers, 5), [(3, 2), (4, 1)])

    def test_zero_array(self):
        numbers = []
        self.assertEqual((two_sum(numbers, 5)), [])

    def test_no_sum(self):
        numbers = []
        self.assertEqual(two_sum(numbers, -5), [])

    def test_same_numbers(self):
        numbers = [2, 2, 2, 2]
        self.assertEqual(two_sum(numbers, 4), [(2, 2,), (2, 2), (2, 2)])


if __name__ == '__main__':
    # numbers = [i for i in range(1000)]
    # print(two_sum(numbers, 200))

    unittest.main()
