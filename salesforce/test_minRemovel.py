import unittest
from minRemovel import Solution

class TestMinRemoval(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().minRemoval

    def test_no_removal_needed(self):
        # All elements within factor 2: [1,2] -> max/min=2 <= k=2, remove 0
        self.assertEqual(self.solve([1, 2], 2), 0)

    def test_all_same(self):
        # All identical: any k works, remove 0
        self.assertEqual(self.solve([3, 3, 3], 1), 0)

    def test_single_element(self):
        # One element is always valid
        self.assertEqual(self.solve([5], 1), 0)

    def test_remove_one(self):
        # [1,2,3,6] k=3: best window [1,2,3] (3/1=3<=3), remove 1 (the 6)
        self.assertEqual(self.solve([1, 2, 3, 6], 3), 1)

    def test_remove_two(self):
        # [1,2,3,6] k=2: best window size 2 (e.g. [3,6]), remove 2
        self.assertEqual(self.solve([1, 2, 3, 6], 2), 2)

    def test_k_equals_1(self):
        # k=1: only identical elements are valid
        # [1,1,2,2] -> best window [1,1] or [2,2] size 2, remove 2
        self.assertEqual(self.solve([1, 1, 2, 2], 1), 2)

    def test_unsorted_input(self):
        # Input order shouldn't matter since we sort internally
        # [6,1,3,2] k=3 -> sorted [1,2,3,6] -> best window [1,2,3], remove 1
        self.assertEqual(self.solve([6, 1, 3, 2], 3), 1)

    def test_large_k_keeps_all(self):
        # k large enough to keep everything
        self.assertEqual(self.solve([1, 10, 100], 100), 0)

    def test_k_too_small_removes_all_but_one(self):
        # [1, 100] k=1: no two elements within factor 1 (100/1=100>1), best window=1
        self.assertEqual(self.solve([1, 100], 1), 1)

    def test_duplicate_elements(self):
        # [2,2,2,10] k=2: best window [2,2,2] (2/2=1<=2), remove 1
        self.assertEqual(self.solve([2, 2, 2, 10], 2), 1)

if __name__ == "__main__":
    unittest.main()
