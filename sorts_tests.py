import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    
    def test_moderate(self):
        nums_selection = [6, 5, 4, 3, 2, 1]
        nums_insertion = [6, 5, 4, 3, 2, 1]
        comps1 = selection_sort(nums_selection)
        comps2 = insertion_sort(nums_insertion)
        self.assertEqual(comps1, 15)
        self.assertEqual(nums_selection, [1, 2, 3, 4, 5, 6])
        self.assertEqual(comps2, 15)
        self.assertEqual(nums_insertion, [1, 2, 3, 4, 5, 6])


if __name__ == '__main__': 
    unittest.main()
