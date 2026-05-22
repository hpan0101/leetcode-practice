# https://leetcode.com/problems/count-of-triplets-that-can-form-two-arrays-of-equal-xor/
'''
Approach: hash map of remainders — O(n^2)
- Count triplets (i < j < k) where (nums[i] + nums[j] + nums[k]) % d == 0.
- For each pair (j, k), the required remainder for nums[i] is:
  target = (d - (nums[j] + nums[k]) % d) % d.
- Maintain a running dict `remainders` of (nums[i] % d -> count) for all i < j.
  Add nums[j] % d to the dict AFTER scanning all k > j, so i < j < k is enforced.
- Look up target in remainders and add its count to the total.
'''
from typing import List
from collections import defaultdict

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        count = 0
        remainders = defaultdict(int)
        n = len(nums)
        for j in range(n):
            for k in range(j + 1, n):
                cur_sum_rem = (nums[j] + nums[k]) % d
                target_rem = (d - cur_sum_rem) % d

                if target_rem in remainders:
                    count += remainders[target_rem]
            remainders[nums[j] % d] += 1
        return count