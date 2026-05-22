# https://leetcode.com/problems/3sum/
'''
Approach: sort + two pointers
- Sort the array so duplicates are adjacent and two-pointer logic works.
- Fix the first element a with the outer loop; skip duplicates of a (i > 0 and
  nums[i] == nums[i-1]).
- Early exit if a > 0 (sorted array means no valid triplet possible).
- Use two pointers l and r to find pairs summing to -a; shrink inward on match,
  skipping duplicate values of l and r to avoid repeated triplets.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i, a, in enumerate(nums):
            if a > 0:
                break
            # dedup
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res