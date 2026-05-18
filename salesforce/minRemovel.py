# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
'''
Approach: sort + sliding window (two pointers)
- Sort nums so the valid window is always contiguous.
- A window [l, r) is valid if all elements are within a factor of k:
  nums[r-1] <= nums[l] * k (max / min <= k).
- Use two pointers: for each l, advance r as far as the window stays valid.
  Since the array is sorted and r never resets, both pointers move forward only -> O(n).
- max_kept = largest valid window found.
- Return n - max_kept (elements outside the best window must be removed).
'''
from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_kept = 0
        r = 0
        n = len(nums)
        for l in range(n):
            while r < n and nums[r] <= nums[l] * k:
                r += 1
            max_kept = max(max_kept, r - l)
        return n - max_kept
        