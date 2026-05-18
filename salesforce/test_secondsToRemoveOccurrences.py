import unittest
from secondsToRemoveOccurrences import Solution

class TestSecondsToRemoveOccurrences(unittest.TestCase):
    def setUp(self):
        self.solve = Solution().secondsToRemoveOccurrences

    def test_leetcode_example_1(self):
        # "0110101" -> 4 seconds
        self.assertEqual(self.solve("0110101"), 4)

    def test_leetcode_example_2(self):
        # "11100" -> all 1s already left of all 0s -> 0 seconds
        self.assertEqual(self.solve("11100"), 0)

    def test_all_zeros(self):
        # No 1s to move -> 0 seconds
        self.assertEqual(self.solve("000"), 0)

    def test_all_ones(self):
        # No 0s -> nothing to swap -> 0 seconds
        self.assertEqual(self.solve("111"), 0)

    def test_single_one_no_zeros(self):
        self.assertEqual(self.solve("1"), 0)

    def test_single_zero(self):
        self.assertEqual(self.solve("0"), 0)

    def test_one_swap_needed(self):
        # "01" -> 1 needs 1 swap to move past the 0
        self.assertEqual(self.solve("01"), 1)

    def test_one_already_left(self):
        # "10" -> 1 is already left of 0 -> 0 seconds
        self.assertEqual(self.solve("10"), 0)

    def test_multiple_zeros_before_one(self):
        # "001" -> 1 must cross 2 zeros -> 2 seconds
        self.assertEqual(self.solve("001"), 2)

    def test_three_zeros_before_one(self):
        # "0001" -> 1 must cross 3 zeros -> 3 seconds
        self.assertEqual(self.solve("0001"), 3)

    def test_two_ones_sequential_wait(self):
        # "0101": first 1 takes 1 sec, second 1 takes max(1+1, 2)=2 sec
        self.assertEqual(self.solve("0101"), 2)

    def test_gap_between_ones(self):
        # "1001": first 1 has no zeros before it (skip),
        # second 1 has 2 zeros before it -> max(0+1, 2)=2 seconds
        self.assertEqual(self.solve("1001"), 2)

    def test_ones_blocked_by_many_zeros(self):
        # "00011": both 1s have 3 zeros before them
        # first 1: max(0+1, 3)=3, second 1: max(3+1, 3)=4
        self.assertEqual(self.solve("00011"), 4)

if __name__ == "__main__":
    unittest.main()
