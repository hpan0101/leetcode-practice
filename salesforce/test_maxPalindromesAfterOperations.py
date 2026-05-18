import unittest
from maxPalindromesAfterOperations import Solution

class TestMaxPalindromes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.solve = self.sol.maxPalindromesAfterOperations

    def test_example_all_can_be_palindromes(self):
        # All 3 words have enough pairs to become palindromes
        self.assertEqual(self.solve(["abbb", "ba", "aa"]), 3)

    def test_example_not_enough_pairs(self):
        # Only 2 out of 3 words can be made palindromes
        self.assertEqual(self.solve(["ab", "cccc", "dddd"]), 2)

    def test_single_char_words(self):
        # Single-char words need 0 pairs — always palindromes
        self.assertEqual(self.solve(["a", "b", "c"]), 3)

    def test_single_word_even_length(self):
        # "aabb" -> 2 pairs, needs 2 pairs for len-4 palindrome
        self.assertEqual(self.solve(["aabb"]), 1)

    def test_single_word_odd_length(self):
        # "abc" -> 0 pairs, needs 1 pair for len-3; can't
        self.assertEqual(self.solve(["abc"]), 0)

    def test_all_same_characters(self):
        # "aaaa" -> 2 pairs, "bb" -> 1 pair; both need 2 and 1 respectively
        self.assertEqual(self.solve(["aaaa", "bb"]), 2)

    def test_greedy_shortest_first_matters(self):
        # Shorter words should be prioritized — sorting ensures this
        # global: a:3, b:3 -> pairs=2; lengths=[2,4]
        # len-2 uses 1 pair (left: 1), len-4 needs 2 but only 1 left -> break
        self.assertEqual(self.solve(["ab", "aabb"]), 1)

    def test_no_pairs_at_all(self):
        # "abcd" -> all unique, 0 pairs; "ef" -> 0 pairs
        # Only words of length 1 (needing 0 pairs) would pass, none here
        self.assertEqual(self.solve(["abcd", "ef"]), 0)

    def test_one_word_length_one(self):
        # Length-1 palindrome always works (needs 0 pairs)
        self.assertEqual(self.solve(["a"]), 1)

    def test_large_pairs_all_pass(self):
        # global: a:3, b:5 -> pairs=3; lengths=[2,4,4]
        # len-2 uses 1 (left: 2), len-4 uses 2 (left: 0), len-4 needs 2 but 0 left -> break
        self.assertEqual(self.solve(["aabb", "bbaa", "ab"]), 2)

if __name__ == "__main__":
    unittest.main()
