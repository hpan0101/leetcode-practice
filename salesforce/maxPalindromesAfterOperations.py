# https://leetcode.com/problems/maximum-palindromes-after-operations/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
'''
Approach: greedy with global character pool
- Since you can swap any character between any two words, only the total
  character frequency matters — not which word each character belongs to.
- Count all characters globally, then compute total available pairs (cnt // 2).
- A palindrome of length L needs exactly L // 2 pairs to fill its symmetric slots
  (odd-length words get one free middle character).
- Sort words by length and greedily assign pairs to the shortest words first,
  maximizing the number of words that can become palindromes.
- Stop as soon as pairs run out (break early).
'''
from collections import Counter
from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        global_count = Counter()
        for word in words:
            global_count.update(word)
        pairs =  sum(cnt // 2 for cnt in global_count.values())
        lengths = sorted(len(word) for word in words)
        res = 0
        for length in lengths:
            needed = length // 2
            if needed <= pairs:
                res += 1
                pairs -= needed
            else:
                break
        return res