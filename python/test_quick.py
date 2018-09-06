import unittest
from quick import swap

class TestStringMethods(unittest.TestCase):

    def test_swap_1(self):
        arr = swap([1,2,3,4,5], 0, 1)
        self.assertEqual(arr, [2,1,3,4,5])

    def test_swap_2(self):
        arr = swap([], 0, 1)
        self.assertEqual(arr, [])


if __name__ == '__main__':
    unittest.main()