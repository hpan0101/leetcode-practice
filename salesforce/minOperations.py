#https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/description/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months
'''
Approach: greedy bit manipulation
- Each operation adds or subtracts a power of 2 from n.
- If n is even, right-shift (n //= 2) to strip trailing zeros — not an operation.
- If n is odd, decide whether to round up or down:
    - n & 3 == 3 (ends in ...11): rounding up clears two 1-bits at once -> n += 1
    - n & 3 == 1 (ends in ...01): single trailing 1-bit -> n -= 1
  Each round up/down counts as one operation.
- Repeat until n == 0.
'''
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n != 0:
            if n % 2 == 0:
                n //= 2
            else:
                if (n & 3) == 3:
                    n += 1
                else:
                    n -= 1
                res += 1
        return res