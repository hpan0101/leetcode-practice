# https://leetcode.com/problems/maximum-or/
'''
Approach: prefix/suffix OR + greedy shift
- You can left-shift exactly one element by k bits (multiply by 2^k) to maximize
  the OR of the entire array.
- Precompute prefix OR (OR of all elements before index i) and suffix OR (OR of
  all elements after index i).
- For each candidate index i, the best OR is: prefix[i] | (nums[i] << k) | suffix[i+1].
- Return the maximum across all candidates.
'''
from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] | nums[i]
        
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]
        max_or_result = 0

        for i in range(n):
            current_or = prefix[i] | (nums[i] << k) | suffix[i + 1]
            max_or_result = max(max_or_result, current_or)
        return max_or_result