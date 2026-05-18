import unittest
from minOperations import Solution

class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().minOperations

    def test_power_of_two(self):
        # n=8 (1000) -> shift down to 1, then -1: 1 operation
        self.assertEqual(self.solve(8), 1)

    def test_n_equals_1(self):
        # 1 -> subtract 2^0: 1 operation
        self.assertEqual(self.solve(1), 1)

    def test_n_equals_2(self):
        # 2 -> shift -> 1 -> subtract: 1 operation
        self.assertEqual(self.solve(2), 1)

    def test_n_equals_3(self):
        # 3 (11) -> round up to 4 -> shift to 1 -> subtract: 2 operations
        # 3 = 4 - 1 = 2^2 - 2^0
        self.assertEqual(self.solve(3), 2)

    def test_n_equals_4(self):
        # 4 -> shift -> 2 -> shift -> 1 -> subtract: 1 operation
        self.assertEqual(self.solve(4), 1)

    def test_n_equals_5(self):
        # 5 (101) -> subtract 1 -> 4 -> shifts -> 1 -> subtract: 2 operations
        # 5 = 4 + 1 = 2^2 + 2^0
        self.assertEqual(self.solve(5), 2)

    def test_n_equals_7(self):
        # 7 (111) -> round up to 8 -> shifts -> 1 -> subtract: 2 operations
        # 7 = 8 - 1 = 2^3 - 2^0
        self.assertEqual(self.solve(7), 2)

    def test_n_equals_39(self):
        # 39 (100111) -> +1 -> 40 -> shifts -> 5 -> -1 -> 4 -> shifts -> 1 -> -1
        # 39 = 32 + 8 - 1 = 2^5 + 2^3 - 2^0: 3 operations
        self.assertEqual(self.solve(39), 3)

    def test_leetcode_example_1(self):
        # LeetCode example: n=2 -> 1 operation
        self.assertEqual(self.solve(2), 1)

    def test_leetcode_example_2(self):
        # LeetCode example: n=3 -> 2 operations
        self.assertEqual(self.solve(3), 2)

    def test_large_power_of_two(self):
        # 1024 = 2^10 -> only 1 operation (subtract 2^10)
        self.assertEqual(self.solve(1024), 1)

    def test_all_ones_bits(self):
        # 15 (1111) -> +1 -> 16 (10000) -> shifts -> 1 -> -1: 2 operations
        # 15 = 16 - 1 = 2^4 - 2^0
        self.assertEqual(self.solve(15), 2)

if __name__ == "__main__":
    unittest.main()
