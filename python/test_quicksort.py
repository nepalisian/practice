import unittest

from quicksort import swap, positive

class QuickSortTest(unittest.TestCase):

    def test_swap_first(self):
        self.assertEqual(swap([1,2,3,4,5], 0, 1), [2,1,3,4,5])

    def test_swap_second(self):
        self.assertEqual(swap([], 0, 1), [])

    def test_positive_first(self):
        self.assertTrue(positive(10))
        self.assertFalse(positive(-10))

if __name__ == "__main__":
    unittest.main()